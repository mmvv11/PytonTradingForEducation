"""
프로그램스러운 프로그램은 다양한 위젯이 있는 것입니다.
화면에 출력되는 UI를 효과적으로 구성하기 위해서는 클래스를 정의하는 것이 좋습니다.
"""

# 이번에는 프로그램에 다양한 위젯을 넣기 위한 준비를 해봅시다.

import sys
from PyQt5.QtWidgets import *


class FirstWindow(QMainWindow):  # 최상위 위젯, QMainWindow를 상속합니다. 일종의 도화지라고 생각합시다.
    def __init__(self):
        super().__init__()  # 이건 우리가 배운 것이었죠!! ㅎㅎ QMainWindow의 생성자를 불러오는 행위입니다.


# 맨 처음 썻던 코드와 같은 패턴입니다. 달라진 것은 UI 구성을 객체지향적으로 했다는 것이겠죠.
app = QApplication(sys.argv)  # QApplication 객체를 생성하고
window = FirstWindow()  # 보여주고 싶은 UI를 구성하여
window.show()  # show 메서드를 호출하고
app.exec_()  # 이벤트 루프를 실행시켜주면 됩니다!
