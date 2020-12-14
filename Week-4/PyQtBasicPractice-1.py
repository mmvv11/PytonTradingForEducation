"""
앞으로는 아래 코드는 프로그램을 생성하기 위한 기본 틀이라고 생각합시다.

정확히 왜 저렇게 되는지 잘 모르겠다구요?
몰라도 됩니다. 모르는 사람도 기능을 구현하기 위해 존재하는 것이 바로 라이브러리이기 때문이죠.
"""

# sys, pyqt 모듈을 사용해서 Hello PyQt 만들어보기.

import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)  # QApplication 객체 생성

label = QLabel("Hello PyQt")  # QLable 객체 생성, "Hello PyQt" 텍스트 셋팅
label.show()  # 객체의 메서드 호출, show()

app.exec_()  # 이벤트 루프 생성

"""
이벤트루프 : 사용자가 프로그램을 종료할 때까지 계속 실행시켜주는 루프
"""
