# Form implementation generated from reading ui file 'create.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 420)
        Dialog.setStyleSheet("background-color: #24222A;")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(parent=Dialog)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(parent=self.frame_3)
        self.label.setGeometry(QtCore.QRect(160, 0, 292, 38))
        self.label.setStyleSheet("font: 700 22pt \"Segoe UI\";\n"
"color: #FFCCCD;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(100, 50, 421, 31))
        self.label_2.setStyleSheet("color: #FFCCCD;\n"
"font: 12pt \"Segoe UI\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.frame_3)
        self.frame = QtWidgets.QFrame(parent=Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rdAvt = QtWidgets.QRadioButton(parent=self.frame)
        self.rdAvt.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.rdAvt.setStyleSheet("border-radius: 500px")
        self.rdAvt.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/Thiết_kế_chưa_có_tên__1_-removebg-preview (1).png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.rdAvt.setIcon(icon)
        self.rdAvt.setIconSize(QtCore.QSize(100, 100))
        self.rdAvt.setObjectName("rdAvt")
        self.horizontalLayout.addWidget(self.rdAvt)
        self.rdAvt_2 = QtWidgets.QRadioButton(parent=self.frame)
        self.rdAvt_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.rdAvt_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../img/Thiết_kế_chưa_có_tên-removebg-preview (1).png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.rdAvt_2.setIcon(icon1)
        self.rdAvt_2.setIconSize(QtCore.QSize(100, 100))
        self.rdAvt_2.setObjectName("rdAvt_2")
        self.horizontalLayout.addWidget(self.rdAvt_2)
        self.rdAvt_3 = QtWidgets.QRadioButton(parent=self.frame)
        self.rdAvt_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.rdAvt_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../img/test.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.rdAvt_3.setIcon(icon2)
        self.rdAvt_3.setIconSize(QtCore.QSize(100, 100))
        self.rdAvt_3.setObjectName("rdAvt_3")
        self.horizontalLayout.addWidget(self.rdAvt_3)
        self.rdAvt_4 = QtWidgets.QRadioButton(parent=self.frame)
        self.rdAvt_4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.rdAvt_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../img/Thiết_kế_chưa_có_tên__2_-removebg-preview.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.rdAvt_4.setIcon(icon3)
        self.rdAvt_4.setIconSize(QtCore.QSize(100, 100))
        self.rdAvt_4.setObjectName("rdAvt_4")
        self.horizontalLayout.addWidget(self.rdAvt_4)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent=Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblName = QtWidgets.QLabel(parent=self.frame_2)
        self.lblName.setEnabled(True)
        self.lblName.setMinimumSize(QtCore.QSize(0, 28))
        self.lblName.setMaximumSize(QtCore.QSize(16777215, 28))
        self.lblName.setStyleSheet("font: 700 10pt \"Segoe UI\";\n"
"color: #A9ADB5;")
        self.lblName.setScaledContents(True)
        self.lblName.setObjectName("lblName")
        self.verticalLayout_2.addWidget(self.lblName)
        self.txtName = QtWidgets.QLineEdit(parent=self.frame_2)
        self.txtName.setMinimumSize(QtCore.QSize(550, 40))
        self.txtName.setMaximumSize(QtCore.QSize(550, 40))
        self.txtName.setBaseSize(QtCore.QSize(20, 20))
        self.txtName.setStyleSheet("background-color: #F6F6F6;\n"
"color: #132742;\n"
"font: 11pt \"Segoe UI\";\n"
"border-radius: 15px;")
        self.txtName.setObjectName("txtName")
        self.verticalLayout_2.addWidget(self.txtName)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(parent=Dialog)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.btnBack = QtWidgets.QPushButton(parent=self.frame_4)
        self.btnBack.setGeometry(QtCore.QRect(20, 20, 101, 31))
        self.btnBack.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnBack.setStyleSheet("font: 700 11pt \"Arial\";\n"
"color: #132742;\n"
"background-color: #E3E5E8;\n"
"border-radius: 5px;")
        self.btnBack.setObjectName("btnBack")
        self.btnCreate = QtWidgets.QPushButton(parent=self.frame_4)
        self.btnCreate.setGeometry(QtCore.QRect(459, 18, 101, 31))
        self.btnCreate.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnCreate.setStyleSheet("background-color: #FFCCCD;\n"
"font: 700 11pt \"Arial\";\n"
"color: #132742;\n"
"border-radius: 5px;")
        self.btnCreate.setObjectName("btnCreate")
        self.verticalLayout.addWidget(self.frame_4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Customise your team"))
        self.label_2.setText(_translate("Dialog", "Give your new team a personality with a name and an icon "))
        self.lblName.setText(_translate("Dialog", "TEAM NAME:"))
        self.btnBack.setText(_translate("Dialog", "Back"))
        self.btnCreate.setText(_translate("Dialog", "Create"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
