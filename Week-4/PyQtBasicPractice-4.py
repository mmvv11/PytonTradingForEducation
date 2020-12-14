"""
각 버튼에 대한 이벤트를 정의해봅니다.
"""

import sys
from PyQt5.QtWidgets import *


class FirstWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 300, 300)  # 윈도우의 위치와 크기를 설정합니다.
        self.setWindowTitle("타이틀셋팅")  # 프로그램 상단에 표시될 타이틀을 설정합니다.

        self.btn1 = QPushButton("버튼1 테스트", self)
        self.btn2 = QPushButton("버튼2 테스트", self)
        self.tv = QLabel("plain text", self)
        self.btn2.move(0, 50)
        self.tv.move(0, 100)

        # btn1에 대한 이벤트 리스너
        self.btn1.clicked.connect(self.btn1_clicked)
        # btn2에 대한 이벤트 리스너
        self.btn2.clicked.connect(self.btn2_clicked)

    def btn1_clicked(self):
        self.tv.setText("버튼1 클릭")

    def btn2_clicked(self):
        self.tv.setText("버튼2 클릭")

# 맨 처음 썻던 코드와 같은 패턴입니다. 달라진 것은 UI 구성을 객체지향적으로 했다는 것이겠죠.
app = QApplication(sys.argv)  # QApplication 객체를 생성하고
window = FirstWindow()  # 보여주고 싶은 UI를 구성하여
window.show()  # show 메서드를 호출하고
app.exec_()  # 이벤트 루프를 실행시켜주면 됩니다!
