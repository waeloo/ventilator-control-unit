# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\user\OneDrive\Bureau\new HMI 01-07\PressureConfig.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PressureConfig(object):
    def Inc(self):
        x=self.lcdNumber_7.intValue()
        if x<55 :
            x=x+1
            self.lcdNumber_7.setProperty("value", x)
        #self.lcdNumber.value=self.lcdNumber.value+0.5
            self.lcdNumber_7.display(x)
            self.label_17.setText(str(x))

    def Dec(self):
        x=self.lcdNumber_7.intValue()
        if x>0 :
            x=x-1
            self.lcdNumber_7.setProperty("value", x)
        #self.lcdNumber.value=self.lcdNumber.value+0.5
            self.lcdNumber_7.display(x)
            self.label_17.setText(str(x))
    def setupUi(self, PressureConfig):
        PressureConfig.setObjectName("PressureConfig")
        PressureConfig.resize(800, 600)
        PressureConfig.setStyleSheet("QWidget { background-color: rgb(58, 58, 58); }")
        self.frame = QtWidgets.QFrame(PressureConfig)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.frame.setStyleSheet("QFrame {\n"
" background-color: #05B8CC;\n"
"    width: 20px;}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(650, 460, 91, 91))
        self.pushButton.setStyleSheet("QPushButton{image: url(:/newPrefix/New folder/back_light.png);\n"
"\n"
"    color: white;\n"
"    background-color:qlineargradient(spread:reflect, x1:0.5, y1:0.5, x2:1, y2:0.5, stop:0 rgba(255, 199, 0, 255), stop:1 rgba(192, 5, 67, 255));\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton:pressed{ background-color: blue; }\n"
"")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda:PressureConfig.close())

        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(110, 290, 171, 51))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(290, 10, 231, 31))
        self.label_7.setObjectName("label_7")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(490, 310, 51, 21))
        self.label_11.setObjectName("label_11")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(530, 290, 71, 71))
        self.pushButton_6.setStyleSheet("image: url(:/newPrefix/New folder/btn-add-normal.png);")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.Inc)

        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(280, 290, 71, 71))
        self.pushButton_7.setStyleSheet("image: url(:/newPrefix/New folder/btn-remove-normal.png);")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.lcdNumber_7 = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber_7.setGeometry(QtCore.QRect(400, 300, 81, 41))
        self.lcdNumber_7.setProperty("intValue", 0)
        self.lcdNumber_7.setObjectName("lcdNumber_7")
        self.pushButton_7.clicked.connect(self.Dec)

        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(30, 20, 171, 141))
        self.frame_2.setStyleSheet("QFrame, QLabel, QToolTip {\n"
"      border: 2px solid green;\n"
"      border-radius: 4px;\n"
"      padding: 2px;\n"
"      background-image: url(images/welcome.png);\n"
"  }\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_17 = QtWidgets.QLabel(self.frame_2)
        self.label_17.setGeometry(QtCore.QRect(50, 90, 71, 31))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame_2)
        self.label_18.setGeometry(QtCore.QRect(40, 0, 91, 71))
        self.label_18.setObjectName("label_18")

        self.retranslateUi(PressureConfig)
        QtCore.QMetaObject.connectSlotsByName(PressureConfig)

    def retranslateUi(self, PressureConfig):
        _translate = QtCore.QCoreApplication.translate
        PressureConfig.setWindowTitle(_translate("PressureConfig", "Form"))
        self.label_6.setText(_translate("PressureConfig", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Disconnect Alarm</span></p><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Pressure Threshold</span></p></body></html>"))
        self.label_7.setText(_translate("PressureConfig", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Pressure Control</span></p></body></html>"))
        self.label_11.setText(_translate("PressureConfig", "<html><head/><body><p><span style=\" color:#ffffff;\"> cmH2O</span></p></body></html>"))
        self.label_17.setText(_translate("PressureConfig", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">....</span></p></body></html>"))
        self.label_18.setText(_translate("PressureConfig", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Paw</span></p></body></html>"))
import ui_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PressureConfig = QtWidgets.QWidget()
    ui = Ui_PressureConfig()
    ui.setupUi(PressureConfig)
    PressureConfig.show()
    sys.exit(app.exec_())
