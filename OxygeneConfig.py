# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\user\OneDrive\Bureau\new HMI 01-07\OxygeneConfig.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OxygeneConfig(object):
    def Inc(self):
        x=self.lcdNumber_2.intValue()
        if x<100 :
            x=x+1
            self.lcdNumber_2.setProperty("value", x)
        #self.lcdNumber.value=self.lcdNumber.value+0.5
            self.lcdNumber_2.display(x)
            self.label_8.setText(str(x))
    def Dec(self):
        x=self.lcdNumber_2.intValue()
        if x>21 :
            x=x-1
            self.lcdNumber_2.setProperty("value", x)
        #self.lcdNumber.value=self.lcdNumber.value+0.5
            self.lcdNumber_2.display(x)
            self.label_8.setText(str(x))
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(851, 600)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(-60, 0, 911, 600))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber_2.setGeometry(QtCore.QRect(413, 270, 91, 41))
        self.lcdNumber_2.setDigitCount(4)
        self.lcdNumber_2.setProperty("intValue", 21)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame)
        self.pushButton_14.setGeometry(QtCore.QRect(270, 250, 91, 91))
        self.pushButton_14.setStyleSheet("image: url(:/newPrefix/New folder/btn-remove-normal.png);")
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.clicked.connect(self.Dec)

        self.pushButton_13 = QtWidgets.QPushButton(self.frame)
        self.pushButton_13.setGeometry(QtCore.QRect(570, 250, 101, 91))
        self.pushButton_13.setStyleSheet("image: url(:/newPrefix/New folder/btn-add-normal.png);")
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(self.Inc)

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(523, 260, 41, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(420, 30, 131, 41))
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(90, 20, 161, 141))
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
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(50, 90, 71, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(50, 0, 81, 71))
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(770, 470, 91, 91))
        self.pushButton.setStyleSheet("image: url(:/newPrefix/New folder/back_light.png);\n"
"background-color: rgb(255, 170, 127);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda:Form.close())


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:26pt;\">%</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Oxygene</span></p></body></html>"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">....</span></p></body></html>"))
        self.label_9.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">FiO2</span></p></body></html>"))
import ui_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_OxygeneConfig()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
