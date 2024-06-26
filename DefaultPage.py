# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\user\OneDrive\Bureau\new HMI 01-07\DefaultPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from InspirationConfig import *
from IERatioConfig import   *
from TidalVolumeConfig import *
from ExpirationConfig import *
from RRConfig import *
from OxygeneConfig import *
from TriggerPressureConfig import *
from FlowConfig import *
from GraphPage import *
from SettingsPage import *
from LoadPatientData import *
from AlarmsConfig import *
from PyQt5.QtWidgets import QWidget
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5.QtCore import QFileInfo, QSettings, QDateTime
from PyQt5.QtWidgets import qApp
from datetime import datetime

class Ui_DefaultPage(object):
    def onDateTimeChanged(self):
        
        datetime=QDateTime.currentDateTime()
 
        print(datetime.toString())


    def AlarmsConfig(self):
        self.window=QtWidgets.QWidget()
        self.ui = Ui_AlarmsConfig()
        self.ui.setupUi(self.window)
        self.window.show()
    def LoadPatientData(self):
        self.window=QtWidgets.QWidget()
        self.ui = Ui_LoadPatientData()
        self.ui.setupUi(self.window)
        self.window.show()
    def InspirationConfig(self):
        self.window=QtWidgets.QWidget()
        self.ui = Ui_InspirationConfig()
        self.ui.setupUi(self.window)
        self.window.show()
    def IERatioConfig(self):
        self.window=QtWidgets.QWidget()
        self.ui = Ui_IERatioConfig()
        self.ui.setupUi(self.window)
        self.window.show()
    def TidalVolumeConfig(self):
        self.window=QtWidgets.QWidget()
        self.ui =Ui_TidalVolumeConfig()
        self.ui.setupUi(self.window)
        self.window.show()
    def ExpirationConfig(self):
        self.window=QtWidgets.QWidget()
        self.ui = Ui_ExpirationConfig()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def RRConfig(self):
        self.window=QtWidgets.QWidget()
        self.ui = Ui_RRConfig()
        self.ui.setupUi(self.window)
        self.window.show()
    def TriggerPressureConfig(self):
        self.window=QtWidgets.QWidget()
        self.ui = Ui_TriggerPressureConfig()
        self.ui.setupUi(self.window)
        self.window.show()
    def OxygeneConfig(self):
        self.window=QtWidgets.QWidget()
        self.ui = Ui_OxygeneConfig()
        self.ui.setupUi(self.window)
        self.window.show()
    def FlowConfig(self):
        self.window=QtWidgets.QWidget()
        self.ui = Ui_FlowConfig()
        self.ui.setupUi(self.window)
        self.window.show()
    def GraphPage(self):
        self.window=QtWidgets.QWidget()
        self.ui = Ui_GraphPage()
        self.ui.setupUi(self.window)
        self.window.show()
    def SettingsPage(self):
        self.window=QtWidgets.QWidget()
        self.ui = Ui_SettingsPage()
        self.ui.setupUi(self.window)
        self.window.show()    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 800)
        Form.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(710, 400, 47, 13))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet("QFrame{\n"
"background-color:#18062a  ;\n"
"    color: #000000;\n"
"\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Graph = QtWidgets.QPushButton(self.frame)
        self.Graph.setGeometry(QtCore.QRect(1060, 330, 120, 120))
        self.Graph.setStyleSheet("QPushButton\n"
"\n"
"{image: url(:/newPrefix/New folder/graph_view_light.png);\n"
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
"\n"
"color: rgb(255, 255, 255);\n"
"\n"
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
        self.Graph.setText("")
        self.Graph.setObjectName("Graph")
        self.Graph.clicked.connect(self.GraphPage)
        self.Graph.clicked.connect(lambda:Form.close())

        self.Modes = QtWidgets.QPushButton(self.frame)
        self.Modes.setGeometry(QtCore.QRect(1060, 190, 120, 120))
        self.Modes.setStyleSheet("\n"
"QPushButton\n"
"\n"
"{image: url(:/newPrefix/New folder/trigger_light.png);\n"
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
        self.Modes.setText("")
        self.Modes.setObjectName("Modes")

        self.Start = QtWidgets.QPushButton(self.frame)
        self.Start.setGeometry(QtCore.QRect(1060, 470, 120, 120))
        self.Start.setStyleSheet("QPushButton\n"
"\n"
"{\n"
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
"\n"
"color: rgb(255, 255, 255);\n"
"\n"
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
        self.Start.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/New folder/start_light.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/New folder/stop_light.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.Start.setIcon(icon)
        self.Start.setIconSize(QtCore.QSize(100, 100))
        self.Start.setCheckable(False)
        self.Start.setObjectName("Start")
        self.InspirationPressure = QtWidgets.QPushButton(self.frame)
        self.InspirationPressure.setGeometry(QtCore.QRect(59, 160, 160, 160))
        self.InspirationPressure.setStyleSheet("QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))\n"
"}\n"
"QPushButton {\n"
"     background-color: #3cbaa2; border: 1px solid black;\n"
"     border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}")
        self.InspirationPressure.setText("")
        self.InspirationPressure.setObjectName("InspirationPressure")
        self.InspirationPressure.clicked.connect(self.InspirationConfig)

        self.IERatio = QtWidgets.QPushButton(self.frame)
        self.IERatio.setGeometry(QtCore.QRect(280, 160, 160, 160))
        self.IERatio.setStyleSheet("QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))\n"
"}\n"
"QPushButton {\n"
"     background-color: #3cbaa2; border: 1px solid black;\n"
"     border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}")
        self.IERatio.setText("")
        self.IERatio.setObjectName("IERatio")
        self.IERatio.clicked.connect(self.IERatioConfig)

        self.TidalVolume = QtWidgets.QPushButton(self.frame)
        self.TidalVolume.setGeometry(QtCore.QRect(490, 160, 160, 160))
        self.TidalVolume.setStyleSheet("QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))\n"
"}\n"
"QPushButton {\n"
"     background-color: #3cbaa2; border: 1px solid black;\n"
"     border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}")
        self.TidalVolume.setText("")
        self.TidalVolume.setObjectName("TidalVolume")
        self.TidalVolume.clicked.connect(self.TidalVolumeConfig)

        self.ExpirationPressure = QtWidgets.QPushButton(self.frame)
        self.ExpirationPressure.setGeometry(QtCore.QRect(59, 360, 160, 160))
        self.ExpirationPressure.setStyleSheet("QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))\n"
"}\n"
"QPushButton {\n"
"     background-color: #3cbaa2; border: 1px solid black;\n"
"     border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}")
        self.ExpirationPressure.setText("")
        self.ExpirationPressure.setObjectName("ExpirationPressure")
        self.ExpirationPressure.clicked.connect(self.ExpirationConfig)

        self.BPM = QtWidgets.QPushButton(self.frame)
        self.BPM.setGeometry(QtCore.QRect(280, 360, 160, 160))
        self.BPM.setStyleSheet("QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))\n"
"}\n"
"QPushButton {\n"
"     background-color: #3cbaa2; border: 1px solid black;\n"
"     border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}")
        self.BPM.setText("")
        self.BPM.setObjectName("BPM")
        self.BPM.clicked.connect(self.RRConfig)

        self.Flow = QtWidgets.QPushButton(self.frame)
        self.Flow.setGeometry(QtCore.QRect(490, 360, 160, 160))
        self.Flow.setStyleSheet("QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))\n"
"}\n"
"QPushButton {\n"
"     background-color: #3cbaa2; border: 1px solid black;\n"
"     border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}")
        self.Flow.setText("")
        self.Flow.setObjectName("Flow")
        self.Flow.clicked.connect(self.FlowConfig)

        self.Settings = QtWidgets.QPushButton(self.frame)
        self.Settings.setGeometry(QtCore.QRect(1060, 610, 120, 120))
        self.Settings.setStyleSheet("QPushButton\n"
"\n"
"{image: url(:/newPrefix/New folder/settings_light.gif);\n"
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
"\n"
"color: rgb(255, 255, 255);\n"
"\n"
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
        self.Settings.setText("")
        self.Settings.setObjectName("Settings")
        self.Settings.clicked.connect(self.SettingsPage)
        self.Settings.clicked.connect(lambda:Form.close())


        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(520, 30, 371, 51))
        self.label.setStyleSheet("background-color: rgb(144, 185, 200);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(120, 170, 41, 21))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(110, 290, 61, 21))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(320, 170, 81, 21))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(520, 170, 101, 21))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(550, 290, 41, 21))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(110, 370, 51, 21))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(110, 490, 51, 21))
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(340, 490, 51, 21))
        self.label_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(540, 370, 51, 21))
        self.label_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(540, 490, 61, 21))
        self.label_12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.Oxygene = QtWidgets.QPushButton(self.frame)
        self.Oxygene.setGeometry(QtCore.QRect(720, 160, 160, 160))
        self.Oxygene.setStyleSheet("QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))\n"
"}\n"
"QPushButton {\n"
"     background-color: #3cbaa2; border: 1px solid black;\n"
"     border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}")
        self.Oxygene.setText("")
        self.Oxygene.setObjectName("Oxygene")
        self.Oxygene.clicked.connect(self.OxygeneConfig)

        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(760, 170, 81, 21))
        self.label_13.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(790, 290, 21, 21))
        self.label_14.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_14.setObjectName("label_14")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(300, 370, 121, 21))
        self.label_16.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(80, 200, 120, 80))
        self.label_17.setStyleSheet("color: rgb(0, 255, 255);")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame)
        self.label_18.setGeometry(QtCore.QRect(300, 200, 120, 80))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(509, 200, 120, 80))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(739, 200, 120, 80))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(80, 400, 120, 80))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(300, 400, 120, 80))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(510, 399, 120, 80))
        self.label_23.setObjectName("label_23")
        self.Ptrig = QtWidgets.QPushButton(self.frame)
        self.Ptrig.setGeometry(QtCore.QRect(719, 360, 160, 160))
        self.Ptrig.setStyleSheet("QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))\n"
"}\n"
"QPushButton {\n"
"     background-color: #3cbaa2; border: 1px solid black;\n"
"     border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}")
        self.Ptrig.setText("")
        self.Ptrig.setObjectName("Ptrig")
        self.Ptrig.clicked.connect(self.TriggerPressureConfig)

        self.label_25 = QtWidgets.QLabel(self.frame)
        self.label_25.setGeometry(QtCore.QRect(740, 400, 120, 80))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.frame)
        self.label_26.setGeometry(QtCore.QRect(770, 490, 61, 21))
        self.label_26.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.frame)
        self.label_27.setGeometry(QtCore.QRect(740, 370, 121, 21))
        self.label_27.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_27.setObjectName("label_27")
        self.Trigger = QtWidgets.QPushButton(self.frame)
        self.Trigger.setGeometry(QtCore.QRect(1060, 50, 120, 120))
        self.Trigger.setStyleSheet("\n"
"QPushButton\n"
"\n"
"{image: url(:/newPrefix/New folder/screen_light.png);\n"
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
        self.Trigger.setText("")
        self.Trigger.setObjectName("Trigger")
        self.Trigger.clicked.connect(self.LoadPatientData)

        self.label_28 = QtWidgets.QLabel(self.frame)
        self.label_28.setGeometry(QtCore.QRect(340, 290, 41, 21))
        self.label_28.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_28.setObjectName("label_28")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setGeometry(QtCore.QRect(50, 20, 120, 80))
        self.stackedWidget.setStyleSheet("image: url(:/newPrefix/New folder/power_critical_light.png);\n"
"background-color: rgb(24, 6, 42);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setStyleSheet("image: url(:/newPrefix/New folder/power_battery_light.png);")
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setStyleSheet("image: url(:/newPrefix/New folder/power_batteryCharging_light.png);")
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setStyleSheet("image: url(:/newPrefix/New folder/power_wall_light.png);")
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.frame)
        self.dateTimeEdit.setGeometry(QtCore.QRect(160, 40, 200, 30))
        self.dateTimeEdit.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.dateTimeEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.dateTimeEdit.setWrapping(False)
        self.dateTimeEdit.setDate(QtCore.QDate(2021, 7, 16))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateTimeEdit.setDisplayFormat("dd/MM/yyyy hh:mm:ss")
        self.dateTimeEdit.dateTimeChanged.connect(self.onDateTimeChanged)


        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(380, 40, 51, 41))
        self.pushButton.setStyleSheet("image: url(:/newPrefix/New folder/disable-alarm.png);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(446, 40, 51, 41))
        self.pushButton_2.setStyleSheet("image: url(:/newPrefix/New folder/icons8-alarm-96.png);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.AlarmsConfig)

        self.Modes.raise_()
        self.Graph.raise_()
        self.Start.raise_()
        self.InspirationPressure.raise_()
        self.IERatio.raise_()
        self.TidalVolume.raise_()
        self.ExpirationPressure.raise_()
        self.BPM.raise_()
        self.Flow.raise_()
        self.Settings.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.Oxygene.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.Ptrig.raise_()
        self.label_25.raise_()
        self.label_26.raise_()
        self.label_27.raise_()
        self.Trigger.raise_()
        self.label_28.raise_()
        self.stackedWidget.raise_()
        self.dateTimeEdit.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; color:#ffffff;\">StarzMed Air-7000</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">PIP</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">cmH20</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">I:E Ratio</span></p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Tidal Volume</span></p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">ml</span></p></body></html>"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">PEEP</span></p></body></html>"))
        self.label_9.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">cmH20</span></p></body></html>"))
        self.label_10.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">BPM</span></p></body></html>"))
        self.label_11.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Flow</span></p></body></html>"))
        self.label_12.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">L/min</span></p></body></html>"))
        self.label_13.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Oxygen</span></p></body></html>"))
        self.label_14.setText(_translate("Form", "<html><head/><body><p align=\"center\">%</p></body></html>"))
        self.label_16.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Respiratory Rate</span></p></body></html>"))
        self.label_17.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">...</span></p></body></html>"))
        self.label_18.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">...</span></p></body></html>"))
        self.label_19.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">...</span></p></body></html>"))
        self.label_20.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">...</span></p></body></html>"))
        self.label_21.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">...</span></p></body></html>"))
        self.label_22.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">...</span></p></body></html>"))
        self.label_23.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">...</span></p></body></html>"))
        self.label_25.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">...</span></p></body></html>"))
        self.label_26.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">cmH20</span></p></body></html>"))
        self.label_27.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Ptrig(Sensitivity)</span></p></body></html>"))
        self.label_28.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">sec</span></p></body></html>"))
import ui_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_DefaultPage()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
