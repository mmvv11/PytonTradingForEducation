"""
빗썸 API를 활용하여 실제 PyQT의 위젯에 데이터를 입력해봅니다.
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pybithumb

form_class = uic.loadUiType("../res/week4-1.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pbBtcPrice.clicked.connect(self.pbBtcPrice_clicked)

    def pbBtcPrice_clicked(self):
        price = pybithumb.get_current_price("BTC")
        self.leBtcPrice.setText(str(price))


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
