"""
API의 개념을 이해하고 활용합니다.

pip install pybithumb
"""

# TODO 과제는 PyQT와 빗썸 public API를 활용해서 비트코인, 이더리움, 리플 등.. 한 3개정도의 시세를 지속적으로 업데이트하는 프로그램 만들기

import pybithumb

# 티커목록 조회 API
tickers = pybithumb.get_tickers()

# 티커 상세정보 조회 API, (시가/고가/저가/종가/거래량) 리턴
details = pybithumb.get_market_detail("BTC")
print(details)

# 티커 현가 조회 API
price = pybithumb.get_current_price("BTC")
