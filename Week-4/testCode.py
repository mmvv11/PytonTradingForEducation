import pybithumb
from privateAPI.pybitumbPrivateAPI import pybithumbPrivateAPI

# 시가, 고가, 저가, 종가, 거래량
btcInfo = pybithumb.get_candlestick("BTC")
# 종가만 가져오고
btcClosePrice = btcInfo['close']
# 5일 이동평균을 계산합니다.
btcMA = btcClosePrice.rolling(5).mean()

a = pybithumbPrivateAPI.get_balance("BTC")[2]

pybithumbPrivateAPI.get_balance("BTC")