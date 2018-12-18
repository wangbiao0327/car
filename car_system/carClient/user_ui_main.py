# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_User_UI(object):
    def setupUi(self, User_UI):
        User_UI.setObjectName("User_UI")
        User_UI.resize(690, 600)
        User_UI.setStyleSheet("QMainWindow{\n"
"\n"
"background-image:\n"
"     url(:/new/prefix1/picture/back.jpg)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(User_UI)
        self.centralwidget.setStyleSheet("QWidget\n"
"{\n"
"\n"
"background-image:\n"
"     url(:/new/prefix1/picture/back.jpg)\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.user_name_label = QtWidgets.QLabel(self.centralwidget)
        self.user_name_label.setGeometry(QtCore.QRect(370, 40, 100, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.user_name_label.setFont(font)
        self.user_name_label.setStyleSheet("QLabel\n"
"{\n"
"background:rgba(0,0,0,0)\n"
"}")
        self.user_name_label.setObjectName("user_name_label")
        self.account_name_label = QtWidgets.QLabel(self.centralwidget)
        self.account_name_label.setGeometry(QtCore.QRect(490, 40, 180, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.account_name_label.setFont(font)
        self.account_name_label.setStyleSheet("QLabel\n"
"{\n"
"background:rgba(0,0,0,0)\n"
"}")
        self.account_name_label.setObjectName("account_name_label")
        self.calendar_widget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendar_widget.setGeometry(QtCore.QRect(230, 210, 450, 350))
        self.calendar_widget.setSelectedDate(QtCore.QDate(2018, 10, 31))
        self.calendar_widget.setMinimumDate(QtCore.QDate(1753, 9, 14))
        self.calendar_widget.setGridVisible(True)
        self.calendar_widget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.LongDayNames)
        self.calendar_widget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendar_widget.setObjectName("calendar_widget")
        self.personal_information_btn = QtWidgets.QPushButton(self.centralwidget)
        self.personal_information_btn.setGeometry(QtCore.QRect(20, 40, 150, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.personal_information_btn.setFont(font)
        self.personal_information_btn.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(166,166,166);\n"
"color:white;\n"
"border:1px solid rgb(168,168,168);\n"
"background:rgba(0,0,0,0);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgba(239,239,239,1);\n"
"color:back;\n"
"background:rgba(166,166,166,1);\n"
"}")
        self.personal_information_btn.setObjectName("personal_information_btn")
        self.stop_car_history_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_car_history_btn.setGeometry(QtCore.QRect(20, 180, 150, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.stop_car_history_btn.setFont(font)
        self.stop_car_history_btn.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(166,166,166);\n"
"color:white;\n"
"border:1px solid rgb(168,168,168);\n"
"background:rgba(0,0,0,0);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgba(239,239,239,1);\n"
"color:back;\n"
"background:rgba(166,166,166,1);\n"
"}")
        self.stop_car_history_btn.setObjectName("stop_car_history_btn")
        self.modify_username_btn = QtWidgets.QPushButton(self.centralwidget)
        self.modify_username_btn.setGeometry(QtCore.QRect(20, 320, 150, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.modify_username_btn.setFont(font)
        self.modify_username_btn.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(166,166,166);\n"
"color:white;\n"
"border:1px solid rgb(168,168,168);\n"
"background:rgba(0,0,0,0);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgba(239,239,239,1);\n"
"color:back;\n"
"background:rgba(166,166,166,1);\n"
"}")
        self.modify_username_btn.setObjectName("modify_username_btn")
        self.modify_password_btn = QtWidgets.QPushButton(self.centralwidget)
        self.modify_password_btn.setGeometry(QtCore.QRect(20, 460, 150, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.modify_password_btn.setFont(font)
        self.modify_password_btn.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(166,166,166);\n"
"color:white;\n"
"border:1px solid rgb(168,168,168);\n"
"background:rgba(0,0,0,0);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgba(239,239,239,1);\n"
"color:back;\n"
"background:rgba(166,166,166,1);\n"
"}")
        self.modify_password_btn.setObjectName("modify_password_btn")
        self.today_weather_label = QtWidgets.QLabel(self.centralwidget)
        self.today_weather_label.setGeometry(QtCore.QRect(370, 120, 300, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.today_weather_label.setFont(font)
        self.today_weather_label.setStyleSheet("QLabel\n"
"{\n"
"background:rgba(0,0,0,0)\n"
"}")
        self.today_weather_label.setObjectName("today_weather_label")
        self.today_weather_name_label = QtWidgets.QLabel(self.centralwidget)
        self.today_weather_name_label.setGeometry(QtCore.QRect(230, 120, 121, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.today_weather_name_label.setFont(font)
        self.today_weather_name_label.setStyleSheet("QLabel\n"
"{\n"
"background:rgba(0,0,0,0)\n"
"}")
        self.today_weather_name_label.setObjectName("today_weather_name_label")
        self.logout_btn = QtWidgets.QPushButton(self.centralwidget)
        self.logout_btn.setGeometry(QtCore.QRect(570, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(14)
        self.logout_btn.setFont(font)
        self.logout_btn.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(166,166,166);\n"
"color:white;\n"
"border:1px solid rgb(168,168,168);\n"
"background:rgba(0,0,0,0);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgba(239,239,239,1);\n"
"color:back;\n"
"background:rgba(166,166,166,1);\n"
"}")
        self.logout_btn.setObjectName("logout_btn")
        User_UI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(User_UI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 18))
        self.menubar.setObjectName("menubar")
        User_UI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(User_UI)
        self.statusbar.setObjectName("statusbar")
        User_UI.setStatusBar(self.statusbar)

        self.retranslateUi(User_UI)
        QtCore.QMetaObject.connectSlotsByName(User_UI)

    def retranslateUi(self, User_UI):
        _translate = QtCore.QCoreApplication.translate
        User_UI.setWindowTitle(_translate("User_UI", "爱停车"))
        self.user_name_label.setText(_translate("User_UI", "<html><head/><body><p><span style=\" color:#00aaff;\">用户名</span></p></body></html>"))
        self.account_name_label.setText(_translate("User_UI", "<html><head/><body><p><span style=\" color:#00aaff;\">17688893888</span></p></body></html>"))
        self.personal_information_btn.setToolTip(_translate("User_UI", "查看个人资料"))
        self.personal_information_btn.setText(_translate("User_UI", "个人资料"))
        self.stop_car_history_btn.setToolTip(_translate("User_UI", "查看历史停车记录"))
        self.stop_car_history_btn.setText(_translate("User_UI", "停车记录"))
        self.modify_username_btn.setToolTip(_translate("User_UI", "修改用户名"))
        self.modify_username_btn.setText(_translate("User_UI", "修改用户名"))
        self.modify_password_btn.setToolTip(_translate("User_UI", "修改登录密码"))
        self.modify_password_btn.setText(_translate("User_UI", "修改密码"))
        self.today_weather_label.setText(_translate("User_UI", "<html><head/><body><p><span style=\" font-size:14pt; color:#00aaff;\">今日天气</span></p></body></html>"))
        self.today_weather_name_label.setText(_translate("User_UI", "<html><head/><body><p><span style=\" font-size:14pt; color:#00aaff;\">今日天气</span></p></body></html>"))
        self.logout_btn.setText(_translate("User_UI", "注销"))

from background import *
