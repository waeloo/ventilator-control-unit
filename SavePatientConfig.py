# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\user\OneDrive\Bureau\new HMI 01-07\SavePatientConfig.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Form(object):
    

    def b0_cb():
        self.label_10.setText(str(0))


    def b1_cb(self):
        self.label_10.setText(str(1))

    def b2_cb():
        self.label_10.setText(str(2))
    def b3_cb():
        self.label_10.setText(str(3))


    def b4_cb():
        self.label_10.setText(str(4))


    def b5_cb():
        self.label_10.setText(str(5))


    def b6_cb():
        self.label_10.setText(str(6))


    def b7_cb():
        self.label_10.setText(str(7))


    def b8_cb():
        self.label_10.setText(str(8))


    def b9_cb():
        self.label_10.setText(str(9))


    def b_clear_cb():
        self.label_10.setText(str(""))


    def b_enter_cb():
            if self.password == g_hardware_settings.dictionary["admin_password"]:
                self.label_10.configure(text=_("Success!"))
                data.save(data.metrics_to_dictionary(g_metric_list), 'data/patientData_default.json')
                self.password = ""
                self.password_dummy = ""
            else:
                self.label_10.configure(text=_("Wrong Password"))
                self.password = ""
                self.password_dummy = ""

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setStyleSheet("background-color: rgb(85, 85, 255);")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.frame_2.setStyleSheet("QFrame[height=\"3\"], QFrame[width=\"3\"] {\n"
"    background-color: #AAA;\n"
"}\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(670, 480, 91, 91))
        self.pushButton.setStyleSheet("QPushButton{image: url(:/newPrefix/New folder/back_dark.png);\n"
"\n"
"border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"QPushButton:pressed{ background-color: orange; }\n"
"")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(240, 10, 311, 41))
        self.label_3.setObjectName("label_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 410, 101, 41))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background-color: #2B5DD1;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;\n"
"}\n"
"QPushButton:pressed{ background-color: orange; }\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(200, 410, 101, 41))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    background-color: #2B5DD1;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightred;\n"
"}\n"
"QPushButton:pressed{ background-color: orange; }\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_6.setGeometry(QtCore.QRect(230, 250, 70, 50))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    background-color: #2B5DD1;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;\n"
"}\n"
"QPushButton:pressed{ background-color: orange; }\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_7.setGeometry(QtCore.QRect(340, 250, 70, 50))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    background-color: #2B5DD1;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;\n"
"}\n"
"QPushButton:pressed{ background-color: orange; }\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_9.setGeometry(QtCore.QRect(230, 172, 70, 50))
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"    background-color: #2B5DD1;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;\n"
"}\n"
"QPushButton:pressed{ background-color: orange; }\n"
"")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_10.setGeometry(QtCore.QRect(340, 172, 70, 50))
        self.pushButton_10.setStyleSheet("QPushButton {\n"
"    background-color: #2B5DD1;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;\n"
"}\n"
"QPushButton:pressed{ background-color: orange; }\n"
"")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_11.setGeometry(QtCore.QRect(460, 170, 70, 50))
        self.pushButton_11.setStyleSheet("QPushButton {\n"
"    background-color: #2B5DD1;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;\n"
"}\n"
"QPushButton:pressed{ background-color: orange; }\n"
"")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_8.setGeometry(QtCore.QRect(460, 250, 70, 50))
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"    background-color: #2B5DD1;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;\n"
"}\n"
"QPushButton:pressed{ background-color: orange; }\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_12.setGeometry(QtCore.QRect(340, 410, 70, 50))
        self.pushButton_12.setStyleSheet("QPushButton {\n"
"    background-color: #2B5DD1;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;\n"
"}\n"
"QPushButton:pressed{ background-color: orange; }\n"
"")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_13.setGeometry(QtCore.QRect(460, 320, 70, 50))
        self.pushButton_13.setStyleSheet("QPushButton {\n"
"    background-color: #2B5DD1;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;\n"
"}\n"
"QPushButton:pressed{ background-color: orange; }\n"
"")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_14.setGeometry(QtCore.QRect(340, 320, 70, 50))
        self.pushButton_14.setStyleSheet("QPushButton {\n"
"    background-color: #2B5DD1;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;\n"
"}\n"
"QPushButton:pressed{ background-color: orange; }\n"
"")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_15.setGeometry(QtCore.QRect(230, 320, 70, 50))
        self.pushButton_15.setStyleSheet("QPushButton {\n"
"    background-color: #2B5DD1;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;\n"
"}\n"
"QPushButton:pressed{ background-color: orange; }\n"
"")
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(240, 50, 311, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(240, 90, 311, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(240, 120, 311, 41))
        self.label_6.setObjectName("label_6")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.frame_3.setStyleSheet("QFrame[height=\"3\"], QFrame[width=\"3\"] {\n"
"    background-color: #AAA;\n"
"}\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(670, 480, 91, 91))
        self.pushButton_2.setStyleSheet("QPushButton{image: url(:/newPrefix/New folder/back_dark.png);\n"
"\n"
"border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"QPushButton:pressed{ background-color: orange; }\n"
"")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda:Form.close())

        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(240, 10, 311, 41))
        self.label_7.setObjectName("label_7")
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_16.setGeometry(QtCore.QRect(450, 440, 101, 41))
        self.pushButton_16.setStyleSheet("QPushButton {\n"
"    background-color: #2B5DD1;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;\n"
"}\n"
"QPushButton:pressed{ background-color: orange; }\n"
"")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_17.setGeometry(QtCore.QRect(200, 440, 101, 41))
        self.pushButton_17.setStyleSheet("QPushButton {\n"
"    background-color: #2B5DD1;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightred;\n"
"}\n"
"QPushButton:pressed{ background-color: orange; }\n"
"")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_18.setGeometry(QtCore.QRect(230, 280, 70, 50))
        self.pushButton_18.setStyleSheet("QPushButton {\n"
"    background-color: #2B5DD1;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;\n"
"}\n"
"QPushButton:pressed{ background-color: orange; }\n"
"")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_19.setGeometry(QtCore.QRect(340, 280, 70, 50))
        self.pushButton_19.setStyleSheet("QPushButton {\n"
"    background-color: #2B5DD1;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;\n"
"}\n"
"QPushButton:pressed{ background-color: orange; }\n"
"")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_20.setGeometry(QtCore.QRect(230, 202, 70, 50))
        self.pushButton_20.setStyleSheet("QPushButton {\n"
"    background-color: #2B5DD1;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;\n"
"}\n"
"QPushButton:pressed{ background-color: orange; }\n"
"")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_20.clicked.connect(self.b1_cb)

        self.pushButton_21 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_21.setGeometry(QtCore.QRect(340, 202, 70, 50))
        self.pushButton_21.setStyleSheet("QPushButton {\n"
"    background-color: #2B5DD1;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;\n"
"}\n"
"QPushButton:pressed{ background-color: orange; }\n"
"")
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_22.setGeometry(QtCore.QRect(460, 200, 70, 50))
        self.pushButton_22.setStyleSheet("QPushButton {\n"
"    background-color: #2B5DD1;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;\n"
"}\n"
"QPushButton:pressed{ background-color: orange; }\n"
"")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_23.setGeometry(QtCore.QRect(460, 280, 70, 50))
        self.pushButton_23.setStyleSheet("QPushButton {\n"
"    background-color: #2B5DD1;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;\n"
"}\n"
"QPushButton:pressed{ background-color: orange; }\n"
"")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_24.setGeometry(QtCore.QRect(340, 440, 70, 50))
        self.pushButton_24.setStyleSheet("QPushButton {\n"
"    background-color: #2B5DD1;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;\n"
"}\n"
"QPushButton:pressed{ background-color: orange; }\n"
"")
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_25.setGeometry(QtCore.QRect(460, 350, 70, 50))
        self.pushButton_25.setStyleSheet("QPushButton {\n"
"    background-color: #2B5DD1;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;\n"
"}\n"
"QPushButton:pressed{ background-color: orange; }\n"
"")
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_26.setGeometry(QtCore.QRect(340, 350, 70, 50))
        self.pushButton_26.setStyleSheet("QPushButton {\n"
"    background-color: #2B5DD1;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;\n"
"}\n"
"QPushButton:pressed{ background-color: orange; }\n"
"")
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_27.setGeometry(QtCore.QRect(230, 350, 70, 50))
        self.pushButton_27.setStyleSheet("QPushButton {\n"
"    background-color: #2B5DD1;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;\n"
"}\n"
"QPushButton:pressed{ background-color: orange; }\n"
"")
        self.pushButton_27.setObjectName("pushButton_27")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(200, 50, 431, 41))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(240, 90, 341, 41))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(230, 150, 311, 41))
        self.label_10.setObjectName("label_10")
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Save Default Patient Data</span></p></body></html>"))
        self.pushButton_4.setText(_translate("Form", "Enter"))
        self.pushButton_5.setText(_translate("Form", "Clear"))
        self.pushButton_6.setText(_translate("Form", "4"))
        self.pushButton_7.setText(_translate("Form", "5"))
        self.pushButton_9.setText(_translate("Form", "1"))
        self.pushButton_10.setText(_translate("Form", "2"))
        self.pushButton_11.setText(_translate("Form", "3"))
        self.pushButton_8.setText(_translate("Form", "6"))
        self.pushButton_12.setText(_translate("Form", "0"))
        self.pushButton_13.setText(_translate("Form", "9"))
        self.pushButton_14.setText(_translate("Form", "8"))
        self.pushButton_15.setText(_translate("Form", "7"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Save Default Patient Data</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Save Default Patient Data</span></p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Save Default Patient Data</span></p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Save Default Patient Data</span></p></body></html>"))
        self.pushButton_16.setText(_translate("Form", "Enter"))
        self.pushButton_17.setText(_translate("Form", "Clear"))
        self.pushButton_18.setText(_translate("Form", "4"))
        self.pushButton_19.setText(_translate("Form", "5"))
        self.pushButton_20.setText(_translate("Form", "1"))
        self.pushButton_21.setText(_translate("Form", "2"))
        self.pushButton_22.setText(_translate("Form", "3"))
        self.pushButton_23.setText(_translate("Form", "6"))
        self.pushButton_24.setText(_translate("Form", "0"))
        self.pushButton_25.setText(_translate("Form", "9"))
        self.pushButton_26.setText(_translate("Form", "8"))
        self.pushButton_27.setText(_translate("Form", "7"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">Save the current configuration as the new patient default</span></p></body></html>"))
        self.label_9.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Enter the administrator password:</span></p></body></html>"))
        self.label_10.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">*****</span></p></body></html>"))
import ui_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
