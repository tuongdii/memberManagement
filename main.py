from PyQt6 import QtWidgets as qtw
from PyQt6 import uic
import sys

class Main(qtw.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi("main.ui", self)
        self.btn_view1.clicked.connect(self.viewDetail)
        self.btn_viewImg1.clicked.connect(self.viewDetail)

        
    def viewDetail(self):
        self.detail = Detail()
        self.detail.show()

class Detail(qtw.QMainWindow):
    def __init__(self):
        super(Detail, self).__init__()
        uic.loadUi("details.ui", self)
        self.btn_back.clicked.connect(lambda:self.close())
               
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec()