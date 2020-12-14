"""
어떻게 하나하나 코드로 디자인을 하고 있을까요? 굉장히 번거로운 일이 아닐 수 없습니다.

Qt Designer 프로그램을 이용해서 윈도우를 손쉽게 디자인해봅시다.
아나콘다를 설치했던 디렉터리에 그것이 있습니다.
C:\Anaconda3\Library\bin

또는 아나콘다 프롬프트창에서 designer를 입력하여 실행시킬 수 있습니다.
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("../res/week4-1.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pbBtcPrice.clicked.connect(self.pbBtcPrice_clicked)

    def pbBtcPrice_clicked(self):
        self.leBtcPrice.setText("이곳에 비트코인 시세가 출력됩니다.")


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
