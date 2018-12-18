# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Manage_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Manage_UI(object):
    def setupUi(self, Manage_UI):
        Manage_UI.setObjectName("Manage_UI")
        Manage_UI.resize(1500, 900)
        Manage_UI.setStyleSheet("QMainWindow\n"
"{\n"
"\n"
"background-color:rgba(100,100,100,0.3);\n"
"\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Manage_UI)
        self.centralwidget.setStyleSheet("QWidget\n"
"{\n"
"    background-color:rgba(100,100,100,0.3);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.manage_stop_car_btn = QtWidgets.QPushButton(self.centralwidget)
        self.manage_stop_car_btn.setGeometry(QtCore.QRect(330, 200, 180, 70))
        self.manage_stop_car_btn.setStyleSheet("QPushButton\n"
"{\n"
"    background-color:rgba(120,120,150,0.5);\n"
"    font-size:32px;\n"
"    color:white;\n"
"}")
        self.manage_stop_car_btn.setObjectName("manage_stop_car_btn")
        self.manage_stop_car_combox = QtWidgets.QComboBox(self.centralwidget)
        self.manage_stop_car_combox.setGeometry(QtCore.QRect(120, 200, 180, 70))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        self.manage_stop_car_combox.setFont(font)
        self.manage_stop_car_combox.setStyleSheet("QComboBox\n"
"{\n"
"    background-color:rgba(100,100,80,0.2);\n"
"    color:red;\n"
"}")
        self.manage_stop_car_combox.setEditable(False)
        self.manage_stop_car_combox.setObjectName("manage_stop_car_combox")
        self.manage_stop_car_display = QtWidgets.QLabel(self.centralwidget)
        self.manage_stop_car_display.setGeometry(QtCore.QRect(120, 350, 400, 100))
        self.manage_stop_car_display.setStyleSheet("QLabel{\n"
"    background-color:rgba(100,100,80,0.5);\n"
"    color:white;\n"
"\n"
"}")
        self.manage_stop_car_display.setObjectName("manage_stop_car_display")
        self.Manage_into_car_picture = QtWidgets.QGroupBox(self.centralwidget)
        self.Manage_into_car_picture.setGeometry(QtCore.QRect(120, 490, 400, 188))
        self.Manage_into_car_picture.setStyleSheet("QGroupBox\n"
"{\n"
"    \n"
"    background-image: url(:/new/prefix1/picture/default-image.jpg);\n"
"}")
        self.Manage_into_car_picture.setTitle("")
        self.Manage_into_car_picture.setObjectName("Manage_into_car_picture")
        self.Manage_leave_car_picture = QtWidgets.QGroupBox(self.centralwidget)
        self.Manage_leave_car_picture.setGeometry(QtCore.QRect(940, 490, 400, 188))
        self.Manage_leave_car_picture.setStyleSheet("QGroupBox\n"
"{\n"
"    \n"
"    background-image: url(:/new/prefix1/picture/default-image.jpg);\n"
"}")
        self.Manage_leave_car_picture.setTitle("")
        self.Manage_leave_car_picture.setObjectName("Manage_leave_car_picture")
        self.manage_system_name_label = QtWidgets.QLabel(self.centralwidget)
        self.manage_system_name_label.setGeometry(QtCore.QRect(0, 0, 1500, 200))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        self.manage_system_name_label.setFont(font)
        self.manage_system_name_label.setStyleSheet("QLabel{\n"
"    background-color:rgba(50,50,50,0);\n"
"    color:white;\n"
"}")
        self.manage_system_name_label.setObjectName("manage_system_name_label")
        self.manage_stop_car_code_title_label = QtWidgets.QLabel(self.centralwidget)
        self.manage_stop_car_code_title_label.setGeometry(QtCore.QRect(130, 740, 300, 100))
        self.manage_stop_car_code_title_label.setStyleSheet("QLabel{\n"
"    background-color:rgba(50,50,50,0);\n"
"    color:white;\n"
"    \n"
"\n"
"}")
        self.manage_stop_car_code_title_label.setObjectName("manage_stop_car_code_title_label")
        self.manage_stop_car_code_value_label = QtWidgets.QLabel(self.centralwidget)
        self.manage_stop_car_code_value_label.setGeometry(QtCore.QRect(380, 740, 300, 100))
        self.manage_stop_car_code_value_label.setStyleSheet("QLabel{\n"
"    background-color:rgba(50,50,50,0);\n"
"    color:white;\n"
"    \n"
"\n"
"}")
        self.manage_stop_car_code_value_label.setObjectName("manage_stop_car_code_value_label")
        self.manage_leave_car_btn = QtWidgets.QPushButton(self.centralwidget)
        self.manage_leave_car_btn.setGeometry(QtCore.QRect(1200, 200, 180, 70))
        self.manage_leave_car_btn.setStyleSheet("QPushButton\n"
"{\n"
"    background-color:rgba(120,120,150,0.5);\n"
"    font-size:32px;\n"
"    color:white;\n"
"}")
        self.manage_leave_car_btn.setObjectName("manage_leave_car_btn")
        self.manage_leave_car_combox = QtWidgets.QComboBox(self.centralwidget)
        self.manage_leave_car_combox.setGeometry(QtCore.QRect(920, 200, 210, 70))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        self.manage_leave_car_combox.setFont(font)
        self.manage_leave_car_combox.setStyleSheet("QComboBox\n"
"{\n"
"    background-color:rgba(100,100,80,0.5);\n"
"    color:red;\n"
"}")
        self.manage_leave_car_combox.setEditable(False)
        self.manage_leave_car_combox.setObjectName("manage_leave_car_combox")
        self.manage_stop_car_code_leave_label = QtWidgets.QLabel(self.centralwidget)
        self.manage_stop_car_code_leave_label.setGeometry(QtCore.QRect(920, 320, 200, 50))
        self.manage_stop_car_code_leave_label.setStyleSheet("QLabel{\n"
"    background-color:rgba(50,50,50,0);\n"
"    color:white;\n"
"    \n"
"\n"
"}")
        self.manage_stop_car_code_leave_label.setObjectName("manage_stop_car_code_leave_label")
        self.manage_leave_input_stop_car_code_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.manage_leave_input_stop_car_code_edit.setGeometry(QtCore.QRect(1150, 320, 300, 50))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(18)
        self.manage_leave_input_stop_car_code_edit.setFont(font)
        self.manage_leave_input_stop_car_code_edit.setStyleSheet("QLineEdit{\n"
"    background-color:rgba(50,50,50,0);\n"
"    color:black;\n"
"    \n"
"\n"
"}")
        self.manage_leave_input_stop_car_code_edit.setClearButtonEnabled(True)
        self.manage_leave_input_stop_car_code_edit.setObjectName("manage_leave_input_stop_car_code_edit")
        self.manage_money_title_label = QtWidgets.QLabel(self.centralwidget)
        self.manage_money_title_label.setGeometry(QtCore.QRect(940, 690, 100, 50))
        self.manage_money_title_label.setStyleSheet("QLabel{\n"
"    background-color:rgba(50,50,50,0);\n"
"    color:white;\n"
"    \n"
"\n"
"}")
        self.manage_money_title_label.setObjectName("manage_money_title_label")
        self.manage_stop_money_label = QtWidgets.QLabel(self.centralwidget)
        self.manage_stop_money_label.setGeometry(QtCore.QRect(1050, 690, 70, 50))
        self.manage_stop_money_label.setStyleSheet("QLabel{\n"
"    background-color:rgba(50,50,50,0.5);\n"
"    color:white;\n"
"    \n"
"\n"
"}")
        self.manage_stop_money_label.setObjectName("manage_stop_money_label")
        self.manage_tooltip_label = QtWidgets.QLabel(self.centralwidget)
        self.manage_tooltip_label.setGeometry(QtCore.QRect(940, 750, 400, 100))
        self.manage_tooltip_label.setStyleSheet("QLabel{\n"
"    background-color:rgba(50,50,50,0);\n"
"    color:white;\n"
"    \n"
"\n"
"}")
        self.manage_tooltip_label.setWordWrap(True)
        self.manage_tooltip_label.setObjectName("manage_tooltip_label")
        self.manage_money_yen_label = QtWidgets.QLabel(self.centralwidget)
        self.manage_money_yen_label.setGeometry(QtCore.QRect(1130, 690, 30, 50))
        self.manage_money_yen_label.setStyleSheet("QLabel{\n"
"    background-color:rgba(50,50,50,0.5);\n"
"    color:white;\n"
"    \n"
"\n"
"}")
        self.manage_money_yen_label.setObjectName("manage_money_yen_label")
        Manage_UI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Manage_UI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1500, 18))
        self.menubar.setObjectName("menubar")
        Manage_UI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Manage_UI)
        self.statusbar.setObjectName("statusbar")
        Manage_UI.setStatusBar(self.statusbar)

        self.retranslateUi(Manage_UI)
        QtCore.QMetaObject.connectSlotsByName(Manage_UI)

    def retranslateUi(self, Manage_UI):
        _translate = QtCore.QCoreApplication.translate
        Manage_UI.setWindowTitle(_translate("Manage_UI", "MainWindow"))
        self.manage_stop_car_btn.setToolTip(_translate("Manage_UI", "<html><head/><body><p><span style=\" font-size:11pt; text-decoration: underline; color:#aa0000;\">模拟停车</span></p></body></html>"))
        self.manage_stop_car_btn.setText(_translate("Manage_UI", "进 入"))
        self.manage_stop_car_combox.setToolTip(_translate("Manage_UI", "<html><head/><body><p><span style=\" font-size:11pt; text-decoration: underline; color:#aa0000;\">选择一辆车停放</span></p></body></html>"))
        self.manage_stop_car_display.setText(_translate("Manage_UI", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\"/></p></body></html>"))
        self.manage_system_name_label.setText(_translate("Manage_UI", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; font-weight:600;\">IStop停车系统</span></p></body></html>"))
        self.manage_stop_car_code_title_label.setText(_translate("Manage_UI", "<html><head/><body><p><span style=\" font-size:36pt;\">停车码：</span></p></body></html>"))
        self.manage_stop_car_code_value_label.setText(_translate("Manage_UI", "<html><head/><body><p><span style=\" font-size:36pt;\"/></p></body></html>"))
        self.manage_leave_car_btn.setToolTip(_translate("Manage_UI", "<html><head/><body><p><span style=\" font-size:11pt; text-decoration: underline; color:#aa0000;\">模拟取车，选择一辆车并输入该车的取车码</span></p></body></html>"))
        self.manage_leave_car_btn.setText(_translate("Manage_UI", "离开"))
        self.manage_leave_car_combox.setToolTip(_translate("Manage_UI", "<html><head/><body><p><span style=\" font-size:11pt; text-decoration: underline; color:#aa0000;\">选择一辆车驶离</span></p></body></html>"))
        self.manage_stop_car_code_leave_label.setText(_translate("Manage_UI", "<html><head/><body><p><span style=\" font-size:18pt;\">输入停车码：</span></p></body></html>"))
        self.manage_leave_input_stop_car_code_edit.setText(_translate("Manage_UI", " "))
        self.manage_money_title_label.setText(_translate("Manage_UI", "<html><head/><body><p><span style=\" font-size:14pt;\">收费:￥</span></p></body></html>"))
        self.manage_stop_money_label.setText(_translate("Manage_UI", "<html><head/><body><p><span style=\" font-size:14pt;\"/></p></body></html>"))
        self.manage_tooltip_label.setText(_translate("Manage_UI", "<html><head/><body><p><span style=\" font-size:14pt;\">欢迎您使用爱停车系统，欢迎您的下次光临。祝您生活愉快！！！</span></p></body></html>"))
        self.manage_money_yen_label.setText(_translate("Manage_UI", "<html><head/><body><p><span style=\" font-size:14pt;\">元</span></p></body></html>"))

from background import *
from stop_car import *
