"""
PyQt 테이블위젯을 사용해서 가상화폐 상세정보를 출력해봅니다.
"""

import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pybithumb

form_class = uic.loadUiType("../res/week4-2.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.twCoins.setRowCount(1)

        timer = QTimer(self)
        timer.start(1000)
        timer.timeout.connect(self.update_details)

    def update_details(self):
        detail = list(pybithumb.get_market_detail('BTC'))
        detail.insert(0, "BTC")
        for i in range(len(detail)):
            self.twCoins.setItem(0, i, QTableWidgetItem(str(detail[i])))


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
