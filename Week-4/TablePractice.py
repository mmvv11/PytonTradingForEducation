import sys
import pybithumb
from PyQt5 import uic
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem

# 티커 목록중 5개만 가져옵니다.
tickers = pybithumb.get_tickers()[:5]
# ui파일을 임포트합니다. 파일명과 경로는 커스텀해야합니다.
form = uic.loadUiType("../res/week4-2.ui")[0]


class TablePractice(QMainWindow, form):
    def __init__(self):
        super(TablePractice, self).__init__()
        # ui 파일을 적용합니다.
        self.setupUi(self)
        # 테이블 행 사이즈를 지정합니다.
        self.twCoins.setRowCount(len(tickers))

        # 타이머를 적용합니다.
        timer = QTimer(self)
        timer.start(1000)
        timer.timeout.connect(self.timeout)

    # 테이블 행에 넣을 데이터를 가져오는 함수
    def get_marget_info(self, ticker):
        # marketInfo = [코인명 ,시가, 고가, 저가, 종가, 거래량]
        marketInfo = list(pybithumb.get_market_detail(ticker))
        marketInfo.insert(0, ticker)
        return marketInfo

    def timeout(self):
        # 반복적으로 테이블 내용을 업데이트 합니다.
        for i, ticker in enumerate(tickers):
            margetInfo = self.get_marget_info(ticker)
            for j in range(len(margetInfo)):
                self.twCoins.setItem(i, j, QTableWidgetItem(str(margetInfo[j])))


app = QApplication(sys.argv)
window = TablePractice()
window.show()
app.exec_()