"""
간단한 전략을 사용해서 가상화폐 자동매매 프로그램을 만들어 봅니다.

5일 이동평균으로 상승장, 하락장을 판단합니다.
티커 목록 중 5개 코인에 대해
코인명, 현재가, 5일 이동평균, 상승장 여부, 보유량을 표시하는 것이 목표입니다.

"""

import sys
import pybithumb
from PyQt5 import uic
from PyQt5.QtCore import QTimer, QThread
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
import pybithumb
import time
import schedule
import threading
from privateAPI.pybitumbPrivateAPI import pybithumbPrivateAPI

# 티커 목록중 5개만 가져옵니다.
tickers = pybithumb.get_tickers()[:5]
# ui파일을 임포트합니다. 파일명과 경로는 커스텀해야합니다.
form = uic.loadUiType("../res/week5-1.ui")[0]


class StrategyPractice(QMainWindow, form):
    def __init__(self):
        super(StrategyPractice, self).__init__()
        # ui 파일을 적용합니다.
        self.setupUi(self)
        # 테이블 행 사이즈를 지정합니다.
        self.twCoins.setRowCount(len(tickers))
        # 자동매매 버튼
        self.pbStartTrade.clicked.connect(self.start_trade)

        # 타이머를 적용합니다.
        timer = QTimer(self)
        timer.start(1000)
        timer.timeout.connect(self.timeout)

    # 테이블 행에 넣을 데이터를 가져오는 함수
    def get_marget_info(self, ticker):
        # [코인명, 현재가, 5일 이동평균, 상승장 여부, 보유량]
        currentPrice = pybithumb.get_current_price(ticker)  # 코인 현재가
        tickerInfo = pybithumb.get_candlestick(ticker)  # 자정 기준 코인 정보
        tickerClosePrice = tickerInfo['close']  # 종가 컬럼
        tickerMA = tickerClosePrice.rolling(5).mean()[-2]  # 종가 컬럼을 이용한 5일간의 이동평균

        if currentPrice > tickerMA:  # 현재 코인의 가격이 5일 이동평균 이상이라면 상승장이라고 판단한다.
            marketState = "Bull Market"
        else:
            marketState = "Bear Market"

        reserve = pybithumbPrivateAPI.get_balance(ticker)[0]  # 현재 보유중인 코인의 수량
        reserve = format(reserve, ".8f")

        result = [ticker, currentPrice, tickerMA, marketState, reserve]
        return result

    def timeout(self):
        # 반복적으로 테이블 내용을 업데이트 합니다.
        for i, ticker in enumerate(tickers):
            marketInfo = self.get_marget_info(ticker)
            for j in range(len(marketInfo)):
                self.twCoins.setItem(i, j, QTableWidgetItem(str(marketInfo[j])))

    def start_trade(self):
        tradeLogic = TradeLogic("BTC")
        tradeLogic.start()  # 스레드 실행


# 매매 로직 클래스 정의
class TradeLogic(threading.Thread):

    def run(self):  # 스레드를 실행할 코드
        self.execute()

    def __init__(self, ticker):
        threading.Thread.__init__(self)  # 스레드 생성자!! 필수!
        self.ticker = ticker
        self.target_price = pybithumb.get_current_price(self.ticker)
        self.current_price = pybithumb.get_current_price(self.ticker)

    # 매도 시도
    def sell(self):
        unit = pybithumbPrivateAPI.get_balance(self.ticker)[0]  # 보유중인 비트코인 수량
        pybithumbPrivateAPI.sell_market_order(self.ticker, unit)  # 매도

    # 매수 시도
    # 지속적으로 현가를 업데이트하면서 변동성 돌파전략에 의해 구매 타이밍을 노린다.
    # 변동성 돌파 전략
    # 매수기준: 당일 변동폭의 k(여기서는 0.5)배 이상 상승하면 해당 가격으로 바로 매수
    # 매도기준: 당일 종가 매도
    def buy(self):
        """
            변동성 돌파전략과 이동평균에 상승장일때만 매수주문을 체결
        """
        if (self.current_price > self.target_price) and (self.current_price > self.get_yesterday_ma()):
            krw = pybithumbPrivateAPI.get_balance(self.ticker)[2]  # 보유중인 원화 조회
            order_book = pybithumb.get_orderbook(self.ticker)  # 코인 호가 정보 조회
            sell_price = order_book['asks'][0]['price']  # 최상단 매도 호가 조회 (가장 저렴하게 매수할 수 있는 가격)
            unit = krw / float(sell_price)  # 현재 잔액으로 매수 가능한 코인 갯수
            pybithumbPrivateAPI.buy_market_order(self.ticker, unit)  # 매수

    # 목표가 갱신
    def update_target_price(self):
        try:
            yesterday_coinInfo = pybithumb.get_candlestick(self.ticker).iloc[-2]
            today_open = yesterday_coinInfo['close']  # 오늘 시가 = 전날 종가
            yesterday_high = yesterday_coinInfo['high']  # 전날 고가
            yesterday_low = yesterday_coinInfo['low']  # 전날 저가
            target_price = today_open + (yesterday_high - yesterday_low) * 0.5  # 목표가 = 오늘 시가 + (전날 변동폭)* 0.5
            now = time.localtime()
            print(f" {self.ticker}, 목표가 갱신 시각:",
                  "%04d/%02d/%02d %02d:%02d:%02d" % (
                      now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))

        except:
            print("목표가 갱신 실패")

        self.sell()  # 매도 시도, 변동성 돌파전략에 의해, 당일 구매한 코인이 있다면 자정에 매도한다.

    def get_yesterday_ma(self):
        df = pybithumb.get_candlestick(self.ticker)
        close = df['close']
        ma = close.rolling(5).mean()
        return ma[-2]

    def execute(self):
        # 매 자정 목표가 갱신 스케쥴러
        # schedule.every().day.at("00:00").do(self.update_target_price)
        schedule.every(3).seconds.do(self.update_target_price)
        while True:
            try:
                schedule.run_pending()
                self.buy()
            except:
                pass
            time.sleep(1)


app = QApplication(sys.argv)
window = StrategyPractice()
window.show()
app.exec_()
