# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\user\OneDrive\Bureau\new HMI 01-07\LoadPatientData.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import json


class Ui_LoadPatientData(object):
    def save(obj, path='patientData.json'):
        print("Saving to file")
        with open(path, 'w') as json_file:
            json.dump(obj, json_file, sort_keys=True, indent=4, separators=(',', ': '))
    def load(path='patientData.json'):
        try: 
            with open(path) as f:
                return json.load(f)
        except IOError:
            return load_default()        
    def load_default(path='patientData_default.json'):
        return json.load(path)


    def printjson(obj):
        print(json.dumps(obj, indent=4, sort_keys=True))


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 800)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet("background-color: rgb(170, 148, 200);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(310, 410, 150, 90))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:0 rgba(10, 242, 251, 255), stop:1 rgba(224, 6, 159, 255));\n"
"    border-radius: 20px;\n"
"image: url(:/newPrefix/New folder/user_load_dark.png);\n"
"\n"
"}\n"
"QPushButton:pressed{ background-color: orange; }")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.load_default)

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 410, 150, 90))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:0 rgba(10, 242, 251, 255), stop:1 rgba(224, 6, 159, 255));\n"
"    border-radius: 20px;\n"
"image: url(:/newPrefix/New folder/user_add_dark.png);\n"
"\n"
"}\n"
"QPushButton:pressed{ background-color: orange; }")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.save)

        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(660, 410, 150, 90))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:0 rgba(10, 242, 251, 255), stop:1 rgba(224, 6, 159, 255));\n"
"    border-radius: 20px;\n"
"image: url(:/newPrefix/New folder/tutorial_dark.png);\n"
"\n"
"}\n"
"QPushButton:pressed{ background-color: orange; }")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(480, 280, 241, 90))
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(830, 410, 150, 90))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:0 rgba(10, 242, 251, 255), stop:1 rgba(224, 6, 159, 255));\n"
"    border-radius: 20px;\n"
"image: url(:/newPrefix/New folder/back_dark.png);\n"
"\n"
"}\n"
"QPushButton:pressed{ background-color: orange; }")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda:Form.close())

        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(380, 160, 150, 90))
        self.widget.setStyleSheet("image: url(:/newPrefix/New folder/robot_dark.png);\n"
"color: white;\n"
"    background-color:qlineargradient(spread:reflect, x1:0.5, y1:0.5, x2:1, y2:0.5, stop:0 rgba(255, 199, 0, 255), stop:1 rgba(192, 5, 67, 255));\n"
"    border-radius: 20px;")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.frame)
        self.widget_2.setGeometry(QtCore.QRect(650, 160, 150, 90))
        self.widget_2.setStyleSheet("image: url(:/newPrefix/New folder/screen_dark.png);\n"
"color: white;\n"
"    background-color:qlineargradient(spread:reflect, x1:0.5, y1:0.5, x2:1, y2:0.5, stop:0 rgba(255, 199, 0, 255), stop:1 rgba(192, 5, 67, 255));\n"
"    border-radius: 20px;")
        self.widget_2.setObjectName("widget_2")
        self.widget_3 = QtWidgets.QWidget(self.frame)
        self.widget_3.setGeometry(QtCore.QRect(520, 160, 150, 90))
        self.widget_3.setStyleSheet("image: url(:/newPrefix/New folder/double_arrow_dark.png);\n"
"color: white;\n"
"    background-color:qlineargradient(spread:reflect, x1:0.5, y1:0.5, x2:1, y2:0.5, stop:0 rgba(255, 199, 0, 255), stop:1 rgba(192, 5, 67, 255));\n"
"    border-radius: 20px;")
        self.widget_3.setObjectName("widget_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(330, 520, 121, 71))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(520, 520, 101, 61))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(700, 520, 81, 51))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(890, 520, 51, 41))
        self.label_5.setObjectName("label_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(1140, 670, 100, 100))
        self.pushButton_5.setStyleSheet("QPushButton\n"
"\n"
"{image: url(:/newPrefix/New folder/power_off_dark.png);\n"
"\n"
"\n"
"background-color: rgb(255, 0, 0);\n"
"\n"
"color: rgb(0, 0, 0);\n"
"\n"
"border-radius:10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"\n"
"{\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton\n"
"\n"
"{\n"
"\n"
"border-style: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"\n"
"{\n"
"\n"
"border-style: solid;\n"
"\n"
"border-color:grey;\n"
"\n"
"border-width: 2px;\n"
"\n"
"}\n"
"QPushButton:pressed{ background-color: green; }\n"
"")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(420, 40, 371, 71))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Hardware initalizing ...</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Load Previous </span></p><p><span style=\" font-size:14pt;\">Patient</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Load New</span></p><p><span style=\" font-size:14pt;\">Patient</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Tutoriel</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Back</span></p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">StarzMed Air-7000</span></p><p align=\"center\"><span style=\" font-size:16pt;\"> Emergency and transport ventilator</span></p></body></html>"))
import ui_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_LoadPatientData()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
