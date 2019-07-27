from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import winreg

class Ui_USBlock(object):
    def lockusb(self):
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                       r"SYSTEM\CurrentControlSet\Services\USBSTOR",
                       0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "Start", 0, winreg.REG_DWORD, 4)
        key2 = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                       r"SYSTEM\CurrentControlSet\Services\USBSTOR\Enum",
                       0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key2, "Count", 0, winreg.REG_DWORD, 0)
        winreg.SetValueEx(key2, "NextInstance", 0, winreg.REG_DWORD, 0)
        try:
            key5 = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                       r"SYSTEM\CurrentControlSet\Services\usbhub",
                       0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key5, "Start", 0, winreg.REG_DWORD, 4)
            key6 = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                           r"SYSTEM\CurrentControlSet\Services\usbhub\Enum",
                           0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key6, "Count", 0, winreg.REG_DWORD, 0)
            winreg.SetValueEx(key6, "NextInstance", 0, winreg.REG_DWORD, 0)    
            key3 = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                       r"SYSTEM\CurrentControlSet\Services\USBHUB3",
                       0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key3, "Start", 0, winreg.REG_DWORD, 4)
            key4 = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                           r"SYSTEM\CurrentControlSet\Services\USBHUB3\Enum",
                           0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key4, "Count", 0, winreg.REG_DWORD, 0)
            winreg.SetValueEx(key4, "NextInstance", 0, winreg.REG_DWORD, 0)
        except:
            self.USBlock.close()
        QMessageBox.about(self.USBlock,"rmnpyt", "USBport is LOCKED!")
        self.USBlock.close()
    def unlockusb(self):
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                       r"SYSTEM\CurrentControlSet\Services\USBSTOR",
                       0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "Start", 0, winreg.REG_DWORD, 3)
        key2 = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                       r"SYSTEM\CurrentControlSet\Services\USBSTOR\Enum",
                       0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key2, "Count", 0, winreg.REG_DWORD, 0)
        winreg.SetValueEx(key2, "NextInstance", 0, winreg.REG_DWORD, 0)
        try:
            key5 = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                       r"SYSTEM\CurrentControlSet\Services\usbhub",
                       0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key5, "Start", 0, winreg.REG_DWORD, 3)
            key6 = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                           r"SYSTEM\CurrentControlSet\Services\usbhub\Enum",
                           0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key6, "Count", 0, winreg.REG_DWORD, 0)
            winreg.SetValueEx(key6, "NextInstance", 0, winreg.REG_DWORD, 0)
            key3 = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                       r"SYSTEM\CurrentControlSet\Services\USBHUB3",
                       0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key3, "Start", 0, winreg.REG_DWORD, 3)
            key4 = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                           r"SYSTEM\CurrentControlSet\Services\USBHUB3\Enum",
                           0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key4, "Count", 0, winreg.REG_DWORD, 0)
            winreg.SetValueEx(key4, "NextInstance", 0, winreg.REG_DWORD, 0)
        except:
            self.USBlock.close()
        QMessageBox.about(self.USBlock,"rmnpyt", "USBport is UNLOCKED!")
        self.USBlock.close()
        
    def setupUi(self, USBlock):
        self.USBlock = USBlock
        USBlock.setObjectName("USBlock")
        USBlock.setFixedSize(320, 240)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(USBlock.sizePolicy().hasHeightForWidth())
        USBlock.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        USBlock.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        USBlock.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(USBlock)
        self.centralwidget.setObjectName("centralwidget")
        self.lockbtn = QtWidgets.QPushButton(self.centralwidget)
        self.lockbtn.setGeometry(QtCore.QRect(40, 70, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lockbtn.setFont(font)
        self.lockbtn.setObjectName("lockbtn")
        self.lockbtn.clicked.connect(self.lockusb)
        self.unlockbtn = QtWidgets.QPushButton(self.centralwidget)
        self.unlockbtn.setGeometry(QtCore.QRect(180, 70, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.unlockbtn.setFont(font)
        self.unlockbtn.setObjectName("unlockbtn")
        self.unlockbtn.clicked.connect(self.unlockusb)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 180, 111, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        USBlock.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(USBlock)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 18))
        self.menubar.setObjectName("menubar")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        USBlock.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(USBlock)
        self.statusbar.setObjectName("statusbar")
        USBlock.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(USBlock)
        self.actionExit.setObjectName("actionExit")
        self.menuExit.addAction(self.actionExit)
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(USBlock)
        self.actionExit.triggered.connect(USBlock.close)
        QtCore.QMetaObject.connectSlotsByName(USBlock)

    def retranslateUi(self, USBlock):
        _translate = QtCore.QCoreApplication.translate
        USBlock.setWindowTitle(_translate("USBlock", "USB LOCK by RamiN"))
        self.lockbtn.setText(_translate("USBlock", "LOCK USB"))
        self.unlockbtn.setText(_translate("USBlock", "unLOCK USB"))
        self.label.setText(_translate("USBlock", "Powered by RamiN"))
        self.menuExit.setTitle(_translate("USBlock", "File"))
        self.actionExit.setText(_translate("USBlock", "exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    USBlock = QtWidgets.QMainWindow()
    ui = Ui_USBlock()
    ui.setupUi(USBlock)
    USBlock.show()
    sys.exit(app.exec_())
