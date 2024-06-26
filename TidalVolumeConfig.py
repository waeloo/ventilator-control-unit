# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\user\OneDrive\Bureau\new HMI 01-07\TidalVolumeConfig.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from vt import *

class Ui_TidalVolumeConfig(object):
    def Inc(self):
        x=self.lcdNumber.intValue()
        if x<2000 :
            x=x+1
            self.lcdNumber.setProperty("value", x)
        #self.lcdNumber.value=self.lcdNumber.value+0.5
            self.lcdNumber.display(x)
            self.label_5.setText(str(x))
            f=open("vt.py","w")
            f.write("vt="+str(x)+"\n")
            f.close
            if f.mode=='r':
                contents= f.read()

    def Dec(self):
        x=self.lcdNumber.intValue()
        if x>150 :
            x=x-1
            self.lcdNumber.setProperty("value", x)
        #self.lcdNumber.value=self.lcdNumber.value+0.5
            self.lcdNumber.display(x)
            self.label_5.setText(str(x))
            f=open("vt.py","w")
            f.write("vt="+str(x)+"\n")
            f.close
            if f.mode=='r':
                contents= f.read()
   

    def setupUi(self, TidalVolumeConfig):
        TidalVolumeConfig.setObjectName("TidalVolumeConfig")
        TidalVolumeConfig.resize(800, 600)
        TidalVolumeConfig.setStyleSheet("background-color: rgb(206, 225, 254);")
        self.frame_2 = QtWidgets.QFrame(TidalVolumeConfig)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.frame_2.setStyleSheet("QFrame {\n"
"font: 75 10pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(660, 480, 91, 91))
        self.pushButton.setStyleSheet("image: url(:/newPrefix/New folder/back_light.png);\n"
"background-color: rgb(170, 255, 255);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda:TidalVolumeConfig.close())

        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(310, 10, 131, 41))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 220, 101, 91))
        self.pushButton_2.setStyleSheet("image: url(:/newPrefix/New folder/btn-remove-normal.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.Dec)

        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(510, 220, 101, 91))
        self.pushButton_3.setStyleSheet("image: url(:/newPrefix/New folder/btn-add-normal.png);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.Inc)

        self.lcdNumber = QtWidgets.QLCDNumber(self.frame_2)
        self.lcdNumber.setGeometry(QtCore.QRect(340, 240, 81, 41))
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.setProperty("intValue", vt)
        self.lcdNumber.setObjectName("lcdNumber")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(30, 30, 131, 111))
        self.frame.setStyleSheet("QFrame, QLabel, QToolTip {\n"
"      border: 2px solid green;\n"
"      border-radius: 4px;\n"
"      padding: 2px;\n"
"      background-image: url(images/welcome.png);\n"
"  }\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(30, 60, 71, 31))
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 0, 71, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(440, 250, 47, 31))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(TidalVolumeConfig)
        QtCore.QMetaObject.connectSlotsByName(TidalVolumeConfig)

    def retranslateUi(self, TidalVolumeConfig):
        _translate = QtCore.QCoreApplication.translate
        TidalVolumeConfig.setWindowTitle(_translate("TidalVolumeConfig", "Form"))
        self.label_3.setText(_translate("TidalVolumeConfig", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Tidal Volume</span></p></body></html>"))
        self.label_5.setText(_translate("TidalVolumeConfig", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">....</span></p></body></html>"))
        self.label.setText(_translate("TidalVolumeConfig", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">VT</span></p></body></html>"))
        self.label_2.setText(_translate("TidalVolumeConfig", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">ml</span></p></body></html>"))
import ui_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TidalVolumeConfig = QtWidgets.QWidget()
    ui = Ui_TidalVolumeConfig()
    ui.setupUi(TidalVolumeConfig)
    TidalVolumeConfig.show()
    sys.exit(app.exec_())
