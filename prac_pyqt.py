import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QCoreApplication

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        #버튼 생성
        btn = QPushButton('push me!', self)
        
        #sizeHint -> 글씨 기준으로 크기를 설정
        btn.resize(btn.sizeHint())
        
        #마우스 대면 해당 버튼 정보
        btn.setToolTip('툴팁입니다')
        
        #버튼위치 변경
        btn.move(50,50)

        #이벤트 발생 -> 해당창 끄기
        btn.clicked.connect(QCoreApplication.instance().quit)

        #창크기, 타이틀
        self.setGeometry(300, 300, 400, 500)
        self.setWindowTitle('The first class')
        
        #기본 창 열기
        self.show()

    #닫을 때 메세지 박스 열기 -> 
    def closeEvent(self, QCloseEvent):
        ans = QMessageBox.question(self, "종료 확인", "종료 하시겠습니까?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if ans == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

#어플리케이션 객체 생성
app = QApplication(sys.argv)
w = Exam()
#이벤트 처리를 위한 메인루프 실행 -> 계속 돌다가 메인루프가 끝나면(창종료, exit실행) -> exit 실행
sys.exit(app.exec_())