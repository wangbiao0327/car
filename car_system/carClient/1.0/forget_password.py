# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forget_password.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from car_client import *


class Ui_Forget_password(object):
    def __init__(self):
        self.widget = QWidget()
        self.setupUi(self.widget)
        self.widget.show()
        self.car_client = carClient()

    def setupUi(self, Forget_password):
        Forget_password.setObjectName("Forget_password")
        Forget_password.resize(840, 395)
        Forget_password.setMaximumSize(QtCore.QSize(840, 395))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        Forget_password.setFont(font)
        self.forget_username_label = QtWidgets.QLabel(Forget_password)
        self.forget_username_label.setGeometry(QtCore.QRect(10, 50, 200, 36))
        self.forget_username_label.setObjectName("forget_username_label")
        self.forget_email_label = QtWidgets.QLabel(Forget_password)
        self.forget_email_label.setGeometry(QtCore.QRect(10, 115, 200, 36))
        self.forget_email_label.setObjectName("forget_email_label")
        self.forget_username_edit = QtWidgets.QLineEdit(Forget_password)
        self.forget_username_edit.setGeometry(QtCore.QRect(240, 50, 346, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.forget_username_edit.setFont(font)
        self.forget_username_edit.setClearButtonEnabled(True)
        self.forget_username_edit.setObjectName("forget_username_edit")
        self.forget_email_edit = QtWidgets.QLineEdit(Forget_password)
        self.forget_email_edit.setGeometry(QtCore.QRect(240, 115, 346, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.forget_email_edit.setFont(font)
        self.forget_email_edit.setClearButtonEnabled(True)
        self.forget_email_edit.setObjectName("forget_email_edit")
        self.forget_submit_btn = QtWidgets.QPushButton(Forget_password)
        self.forget_submit_btn.setGeometry(QtCore.QRect(300, 310, 100, 43))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.forget_submit_btn.setFont(font)
        self.forget_submit_btn.setObjectName("forget_submit_btn")
        self.forget_verification_code_label = QtWidgets.QLabel(Forget_password)
        self.forget_verification_code_label.setGeometry(
            QtCore.QRect(10, 180, 200, 36))
        self.forget_verification_code_label.setObjectName(
            "forget_verification_code_label")
        self.forget_verification_code_edit = QtWidgets.QLineEdit(
            Forget_password)
        self.forget_verification_code_edit.setGeometry(
            QtCore.QRect(240, 180, 346, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.forget_verification_code_edit.setFont(font)
        self.forget_verification_code_edit.setClearButtonEnabled(True)
        self.forget_verification_code_edit.setObjectName(
            "forget_verification_code_edit")
        self.forget_get_verification_btn = QtWidgets.QPushButton(
            Forget_password)

        self.forget_get_verification_btn.clicked.connect(self.get_verification_code)

        self.forget_get_verification_btn.setGeometry(
            QtCore.QRect(620, 115, 200, 43))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.forget_get_verification_btn.setFont(font)
        self.forget_get_verification_btn.setObjectName(
            "forget_get_verification_btn")
        self.forget_cancle_btn = QtWidgets.QPushButton(Forget_password)
        ##
        self.forget_cancle_btn.clicked.connect(self.close)

        self.forget_cancle_btn.setGeometry(QtCore.QRect(490, 310, 100, 43))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.forget_cancle_btn.setFont(font)
        self.forget_cancle_btn.setObjectName("forget_cancle_btn")
        self.forget_tooltip_label = QtWidgets.QLabel(Forget_password)
        self.forget_tooltip_label.setGeometry(QtCore.QRect(210, 245, 600, 45))
        self.forget_tooltip_label.setObjectName("forget_tooltip_label")

        self.retranslateUi(Forget_password)
        QtCore.QMetaObject.connectSlotsByName(Forget_password)

    def retranslateUi(self, Forget_password):
        _translate = QtCore.QCoreApplication.translate
        Forget_password.setWindowTitle(_translate("Forget_password", "忘记密码"))
        self.forget_username_label.setText(_translate(
            "Forget_password", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">用户名</span></p></body></html>"))
        self.forget_email_label.setText(_translate(
            "Forget_password", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">注册邮箱</span></p></body></html>"))
        self.forget_submit_btn.setToolTip(_translate(
            "Forget_password", "<html><head/><body><p><span style=\" font-size:20pt;\">提交验证信息</span></p></body></html>"))
        self.forget_submit_btn.setText(_translate("Forget_password", "提交"))
        self.forget_verification_code_label.setText(_translate(
            "Forget_password", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">验证码</span></p></body></html>"))
        self.forget_get_verification_btn.setToolTip(_translate(
            "Forget_password", "<html><head/><body><p><span style=\" font-size:20pt;\">邮箱获取验证码</span></p></body></html>"))
        self.forget_get_verification_btn.setText(
            _translate("Forget_password", "获取验证码"))
        self.forget_cancle_btn.setToolTip(_translate(
            "Forget_password", "<html><head/><body><p><span style=\" font-size:20pt;\">取消验证</span></p></body></html>"))
        self.forget_cancle_btn.setText(_translate("Forget_password", "取消"))

    def close(self):
        self.widget.close()

    def get_verification_code(self):

        login_account = self.forget_username_edit.text()
        login_email = self.forget_email_edit.text()

        #判断邮箱输入且格式正确
        if login_email:

            self.forget_tooltip_label.setText("")
            judge_result = self.judge_email(login_email)

            if judge_result:
                self.forget_tooltip_label.setText("验证码已发送，请耐心等待...")

            else:
                self.forget_tooltip_label.setText("请输入合法邮箱")
            
        else:
            self.forget_tooltip_label.setText("邮箱不能为空")#没有输入注册邮箱提示邮箱不能为空

        #账户传入，调用client对象
        self.forget_verification_code = self.car_client.forget(login_account, login_email)
        print(self.forget_verification_code)

        try:
            if type(int(self.forget_verification_code)) is not int:
                self.forget_tooltip_label.setText("您输入的账号不存在，请检查后再输入")
        except ValueError:
            self.forget_tooltip_label.setText(self.forget_verification_code)

    def judge_email(self, login_email):
        import re

        pettern = r"\w+@\w+\.[a-z]+"
        L_result = re.findall(pettern, login_email)
        print(L_result)
        if L_result:
            if len(login_email) == len(L_result[0]):
                return True
        
        return False
        



if __name__ == "__main__":

    app = QApplication(sys.argv)
    new = Ui_Forget_password()
    sys.exit(app.exec_())
