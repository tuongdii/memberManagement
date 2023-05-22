from PyQt6 import QtWidgets as qtw
from PyQt6 import uic
import sys
import re

page = 1
class Main(qtw.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi("main.ui", self)
        self.btn_view1.clicked.connect(self.updatePage)
        self.btn_viewImg1.clicked.connect(self.updatePage)
        self.btn_view1.clicked.connect(self.viewDetail)
        self.btn_viewImg1.clicked.connect(self.viewDetail)
        
        self.btn_view2.clicked.connect(self.updatePage)
        self.btn_viewImg2.clicked.connect(self.updatePage)
        self.btn_view2.clicked.connect(self.viewDetail)
        self.btn_viewImg2.clicked.connect(self.viewDetail)
       
        self.btn_view3.clicked.connect(self.updatePage)
        self.btn_viewImg3.clicked.connect(self.updatePage)
        self.btn_view3.clicked.connect(self.viewDetail)
        self.btn_viewImg3.clicked.connect(self.viewDetail)
        
        self.btn_view4.clicked.connect(self.updatePage)
        self.btn_viewImg4.clicked.connect(self.updatePage)
        self.btn_view4.clicked.connect(self.viewDetail)
        self.btn_viewImg4.clicked.connect(self.viewDetail)
        
        self.btn_view5.clicked.connect(self.updatePage)
        self.btn_viewImg5.clicked.connect(self.updatePage)
        self.btn_view5.clicked.connect(self.viewDetail)
        self.btn_viewImg5.clicked.connect(self.viewDetail)
        
        self.btn_view6.clicked.connect(self.updatePage)
        self.btn_viewImg6.clicked.connect(self.updatePage)
        self.btn_view6.clicked.connect(self.viewDetail)
        self.btn_viewImg6.clicked.connect(self.viewDetail)
        
    def viewDetail(self):
        self.detail = Detail()
        self.detail.show()
        
    def updatePage(self):
        global page
        button_name = self.sender().objectName()
        page_number = re.search(r'\d+', button_name)
        if page_number:
            page = int(page_number.group())
        

        
class Detail(qtw.QMainWindow):
    def __init__(self):
        super(Detail, self).__init__()
        pageName = "details" + str(page) + ".ui"
        uic.loadUi(pageName, self)
        self.btn_back.clicked.connect(lambda:self.close())


               
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec()