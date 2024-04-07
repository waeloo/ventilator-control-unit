# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\user\OneDrive\Bureau\new HMI 01-07\ExpirationConfig.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from peep import *




class Ui_ExpirationConfig(object):
    global x
   
    def Inc(self):
        x=self.lcdNumber_3.intValue()
        if x<25 :
            x=self.lcdNumber_3.intValue()
            x=x+1
            self.lcdNumber_3.setProperty("value", x)
            self.lcdNumber_3.display(x)

            self.label_8.setText(str(x))
            f=open("peep.py","w")
            f.write("peep="+str(x)+"\n")
            f.close


            
    def Dec(self):
        x=self.lcdNumber_3.intValue()
        if x>0 :
            x=x-1
            self.lcdNumber_3.setProperty("value", x)
            self.lcdNumber_3.display(x)
            self.label_8.setText(str(x))
            f=open("peep.py","w")
            f.write("peep="+str(x)+"\n")
            f.close

            

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.frame.setStyleSheet("QFrame {\n"
"      background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0.00480769 rgba(3, 50, 76, 255),stop:0.293269 rgba(6, 82, 125, 255),stop:0.514423 rgba(8, 117, 178, 255),stop:0.745192 rgba(7, 108, 164, 255),stop:1 rgba(3, 51, 77, 255));\n"
"    color: #000000;\n"
"\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(690, 490, 91, 91))
        self.pushButton.setStyleSheet("image: url(:/newPrefix/New folder/back_light.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda:Form.close())

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(110, 250, 171, 51))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(310, 20, 191, 41))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(480, 260, 41, 21))
        self.label_6.setObjectName("label_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(540, 240, 71, 71))
        self.pushButton_8.setStyleSheet("image: url(:/newPrefix/New folder/btn-add-normal.png);")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.Inc)

        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(290, 240, 71, 71))
        self.pushButton_9.setStyleSheet("image: url(:/newPrefix/New folder/btn-remove-normal.png);")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.Dec)

        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(40, 20, 161, 141))
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
        self.label_8.setGeometry(QtCore.QRect(30, 90, 71, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(30, 0, 81, 71))
        self.label_9.setObjectName("label_9")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber_3.setGeometry(QtCore.QRect(390, 250, 81, 41))
        self.lcdNumber_3.setProperty("value", 0)

        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.lcdNumber_3.setProperty("intValue", peep)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Disconnect Alarm</span></p><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Pressure Threshold</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Expiration Pressure </span></p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">cmH2O</span></p></body></html>"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">....</span></p></body></html>"))
        self.label_9.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#ffffff;\">PEEP</span></p></body></html>"))
import ui_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_ExpirationConfig()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
