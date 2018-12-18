# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from car_client import *
from register_dialog import *
from forget_password import *

class Ui_Login(object):
    def __init__(self):
        self.widget = QWidget()
        self.setupUi(self.widget)
        self.car_client = carClient()
        self.widget.show()

    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(700, 600)
        Login.setMaximumSize(QtCore.QSize(700, 600))
        Login.setMouseTracking(False)
        self.login_password_lineEdit = QtWidgets.QLineEdit(Login)
        self.login_password_lineEdit.setGeometry(QtCore.QRect(249, 223, 346, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.login_password_lineEdit.setFont(font)
        self.login_password_lineEdit.setMouseTracking(True)
        self.login_password_lineEdit.setFrame(True)
        self.login_password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_password_lineEdit.setReadOnly(False)
        self.login_password_lineEdit.setPlaceholderText("")
        self.login_password_lineEdit.setClearButtonEnabled(True)
        self.login_password_lineEdit.setObjectName("login_password_lineEdit")
        self.login_username_lineEdit = QtWidgets.QLineEdit(Login)
        self.login_username_lineEdit.setGeometry(QtCore.QRect(249, 130, 346, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.login_username_lineEdit.setFont(font)
        self.login_username_lineEdit.setMouseTracking(True)
        self.login_username_lineEdit.setClearButtonEnabled(True)
        self.login_username_lineEdit.setObjectName("login_username_lineEdit")
        self.login_password_label = QtWidgets.QLabel(Login)
        self.login_password_label.setGeometry(QtCore.QRect(6, 223, 200, 36))
        self.login_password_label.setObjectName("login_password_label")
        self.login_regist_btn = QtWidgets.QPushButton(Login)

        ##
        self.login_regist_btn.clicked.connect(self.register_function)

        self.login_regist_btn.setGeometry(QtCore.QRect(455, 380, 100, 43))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.login_regist_btn.setFont(font)
        self.login_regist_btn.setCheckable(False)
        self.login_regist_btn.setObjectName("login_regist_btn")
        self.login_username_label = QtWidgets.QLabel(Login)
        self.login_username_label.setGeometry(QtCore.QRect(6, 130, 200, 36))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.login_username_label.setFont(font)
        self.login_username_label.setObjectName("login_username_label")
        self.login_login_btn = QtWidgets.QPushButton(Login)

        ##
        self.login_login_btn.clicked.connect(self.login_function)

        self.login_login_btn.setGeometry(QtCore.QRect(289, 380, 100, 43))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.login_login_btn.setFont(font)
        self.login_login_btn.setCheckable(False)
        self.login_login_btn.setObjectName("login_login_btn")
        self.login_forget_password_btn = QtWidgets.QPushButton(Login)

        ##忘记密码
        self.login_forget_password_btn.clicked.connect(self.forget_password_function)
        self.login_forget_password_btn.setGeometry(QtCore.QRect(290, 480, 200, 50))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.login_forget_password_btn.setFont(font)
        self.login_forget_password_btn.setText("忘记密码")
        self.login_forget_password_btn.setCheckable(False)
        self.login_forget_password_btn.setObjectName("login_forget_password_btn")
        self.login_tooltip_label = QtWidgets.QLabel(Login)
        self.login_tooltip_label.setGeometry(QtCore.QRect(200, 300, 400, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.login_tooltip_label.setFont(font)
        self.login_tooltip_label.setText("")
        self.login_tooltip_label.setObjectName("login_tooltip_label")
        self.login_welcom_label = QtWidgets.QLabel(Login)
        self.login_welcom_label.setGeometry(QtCore.QRect(115, 19, 541, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.login_welcom_label.setFont(font)
        self.login_welcom_label.setObjectName("login_welcom_label")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "登录爱停车"))
        self.login_password_label.setText(_translate("Login", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">密 码</span></p></body></html>"))
        self.login_regist_btn.setText(_translate("Login", "注册"))
        self.login_username_label.setText(_translate("Login", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#000000;\">用户名</span></p></body></html>"))
        self.login_login_btn.setText(_translate("Login", "登录"))
        self.login_welcom_label.setText(_translate("Login", "<html><head/><body><p><span style=\" color:#550000;\">🌊🌊</span>欢迎您登录爱停车<span style=\" color:#aa0000;\">💖🚗</span></p></body></html>"))

    def login_function(self):
        user_name = self.login_username_lineEdit.text()
        pass_word = self.login_password_lineEdit.text()
        L = [user_name, pass_word]
        print(L)
        result = self.car_client.login(account=user_name,password=pass_word)
        self.login_tooltip_label.setText(result)

    def register_function(self):
        new = Ui_Register()
        new.show()
        

    def forget_password_function(self):
        new = Ui_Forget_password()







       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Ui_Login()
    sys.exit(app.exec_())