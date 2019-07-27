from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from USBlock import Ui_USBlock

class Ui_getPass(object):
    
    def setupUi(self, getPass):
        self.getPass = getPass
        getPass.setObjectName("getPass")
        getPass.resize(320, 120)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        getPass.setWindowIcon(icon)
        self.lineEdit = QtWidgets.QLineEdit(getPass)
        self.lineEdit.setGeometry(QtCore.QRect(140, 30, 161, 21))
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(getPass)
        self.label.setGeometry(QtCore.QRect(20, 30, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.open = QtWidgets.QPushButton(getPass)
        self.open.setGeometry(QtCore.QRect(140, 70, 75, 23))
        self.open.setObjectName("open")
        self.open.clicked.connect(self.checkpass)
        self.close = QtWidgets.QPushButton(getPass)
        self.close.setGeometry(QtCore.QRect(230, 70, 75, 23))
        self.close.setObjectName("close")
        self.close.clicked.connect(getPass.close)

        self.retranslateUi(getPass)
        QtCore.QMetaObject.connectSlotsByName(getPass)
    
    def checkpass(self):
        if self.lineEdit.text() == 'password':
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_USBlock()
            self.ui.setupUi(self.window)
            self.window.show()
            self.getPass.close()
        else:
            QMessageBox.about(self.getPass,"rmnpyt", "WRONG Password!!")

    def retranslateUi(self, getPass):
        _translate = QtCore.QCoreApplication.translate
        getPass.setWindowTitle(_translate("getPass", "Enter Password"))
        self.label.setText(_translate("getPass", "Enter Password :"))
        self.open.setText(_translate("getPass", "ENTER"))
        self.close.setText(_translate("getPass", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    getPass = QtWidgets.QDialog()
    ui = Ui_getPass()
    ui.setupUi(getPass)
    getPass.show()
    sys.exit(app.exec_())
