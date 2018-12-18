# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_dia.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(700, 600)
        Login.setMinimumSize(QtCore.QSize(0, 0))
        Login.setMaximumSize(QtCore.QSize(700, 600))
        Login.setStyleSheet("QDialog{\n"
"\n"
"background-image:\n"
"     url(:/new/prefix1/picture/water_zhu_heibai.jpg);\n"
"}")
        self.login_forget_password_btn = QtWidgets.QPushButton(Login)
        self.login_forget_password_btn.setGeometry(QtCore.QRect(294, 510, 200, 50))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.login_forget_password_btn.setFont(font)
        self.login_forget_password_btn.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(166,166,166);\n"
"color:rgb(0,30,131);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgb(239,239,239);\n"
"color:back;\n"
"}")
        self.login_forget_password_btn.setText("忘记密码")
        self.login_forget_password_btn.setCheckable(False)
        self.login_forget_password_btn.setObjectName("login_forget_password_btn")
        self.login_password_label = QtWidgets.QLabel(Login)
        self.login_password_label.setGeometry(QtCore.QRect(10, 253, 200, 36))
        self.login_password_label.setObjectName("login_password_label")
        self.login_login_btn = QtWidgets.QPushButton(Login)
        self.login_login_btn.setGeometry(QtCore.QRect(293, 410, 100, 43))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.login_login_btn.setFont(font)
        self.login_login_btn.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(166,166,166);\n"
"color:rgb(0,30,131);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgb(239,239,239);\n"
"color:back;\n"
"}")
        self.login_login_btn.setCheckable(False)
        self.login_login_btn.setObjectName("login_login_btn")
        self.login_tooltip_label = QtWidgets.QLabel(Login)
        self.login_tooltip_label.setGeometry(QtCore.QRect(204, 330, 400, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.login_tooltip_label.setFont(font)
        self.login_tooltip_label.setText("")
        self.login_tooltip_label.setObjectName("login_tooltip_label")
        self.login_regist_btn = QtWidgets.QPushButton(Login)
        self.login_regist_btn.setGeometry(QtCore.QRect(459, 410, 100, 43))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.login_regist_btn.setFont(font)
        self.login_regist_btn.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(166,166,166);\n"
"color:rgb(0,30,131);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgb(239,239,239);\n"
"color:back;\n"
"}")
        self.login_regist_btn.setCheckable(False)
        self.login_regist_btn.setObjectName("login_regist_btn")
        self.login_password_lineEdit = QtWidgets.QLineEdit(Login)
        self.login_password_lineEdit.setGeometry(QtCore.QRect(253, 253, 346, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.login_password_lineEdit.setFont(font)
        self.login_password_lineEdit.setMouseTracking(True)
        self.login_password_lineEdit.setStyleSheet("QLineEdit\n"
"{\n"
"color:rgb(0,0,127);\n"
"}")
        self.login_password_lineEdit.setFrame(True)
        self.login_password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_password_lineEdit.setReadOnly(False)
        self.login_password_lineEdit.setPlaceholderText("")
        self.login_password_lineEdit.setClearButtonEnabled(True)
        self.login_password_lineEdit.setObjectName("login_password_lineEdit")
        self.login_username_lineEdit = QtWidgets.QLineEdit(Login)
        self.login_username_lineEdit.setGeometry(QtCore.QRect(253, 160, 346, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.login_username_lineEdit.setFont(font)
        self.login_username_lineEdit.setMouseTracking(True)
        self.login_username_lineEdit.setStyleSheet("QLineEdit\n"
"{\n"
"color:rgb(0,0,127);\n"
"}")
        self.login_username_lineEdit.setClearButtonEnabled(True)
        self.login_username_lineEdit.setObjectName("login_username_lineEdit")
        self.login_welcom_label = QtWidgets.QLabel(Login)
        self.login_welcom_label.setGeometry(QtCore.QRect(119, 49, 541, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.login_welcom_label.setFont(font)
        self.login_welcom_label.setObjectName("login_welcom_label")
        self.login_username_label = QtWidgets.QLabel(Login)
        self.login_username_label.setGeometry(QtCore.QRect(10, 160, 200, 36))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.login_username_label.setFont(font)
        self.login_username_label.setStyleSheet("QLabel{\n"
"    \n"
"}")
        self.login_username_label.setObjectName("login_username_label")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "登录爱停车"))
        self.login_password_label.setText(_translate("Login", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#00007f;\">密 码</span></p></body></html>"))
        self.login_login_btn.setText(_translate("Login", "登录"))
        self.login_regist_btn.setText(_translate("Login", "注册"))
        self.login_welcom_label.setText(_translate("Login", "<html><head/><body><p><span style=\" color:#550000;\">🌊🌊</span>欢迎您登录爱停车<span style=\" color:#aa0000;\">💖🚗</span></p></body></html>"))
        self.login_username_label.setText(_translate("Login", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#00007f;\">用户名</span></p></body></html>"))

from background import *
