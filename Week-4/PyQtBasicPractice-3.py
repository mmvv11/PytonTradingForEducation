"""
이제는 실제로 QLable 이외에 다양한 위젯을 넣어보겠습니다.
"""

import sys
from PyQt5.QtWidgets import *


class FirstWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 300, 300)  # 윈도우의 위치와 크기를 설정합니다.
        self.setWindowTitle("타이틀셋팅")  # 프로그램 상단에 표시될 타이틀을 설정합니다.

        btn1 = QPushButton("버튼1 테스트", self)
        btn2 = QPushButton("버튼2 테스트", self)
        btn2.move(0, 50)


# 맨 처음 썻던 코드와 같은 패턴입니다. 달라진 것은 UI 구성을 객체지향적으로 했다는 것이겠죠.
app = QApplication(sys.argv)  # QApplication 객체를 생성하고
window = FirstWindow()  # 보여주고 싶은 UI를 구성하여
window.show()  # show 메서드를 호출하고
app.exec_()  # 이벤트 루프를 실행시켜주면 됩니다!
