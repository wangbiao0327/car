# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forget_dia.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Forget_Password(object):
    def setupUi(self, Forget_Password):
        Forget_Password.setObjectName("Forget_Password")
        Forget_Password.resize(840, 395)
        Forget_Password.setMaximumSize(QtCore.QSize(840, 395))
        Forget_Password.setStyleSheet("QDialog{\n"
"\n"
"background-image:\n"
"     url(:/new/prefix1/picture/water_zhu_heibai.jpg)\n"
"}")
        self.forget_submit_btn = QtWidgets.QPushButton(Forget_Password)
        self.forget_submit_btn.setGeometry(QtCore.QRect(300, 300, 100, 43))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.forget_submit_btn.setFont(font)
        self.forget_submit_btn.setStyleSheet("QPushButton\n"
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
        self.forget_submit_btn.setObjectName("forget_submit_btn")
        self.forget_username_label = QtWidgets.QLabel(Forget_Password)
        self.forget_username_label.setGeometry(QtCore.QRect(10, 40, 200, 36))
        self.forget_username_label.setObjectName("forget_username_label")
        self.forget_username_edit = QtWidgets.QLineEdit(Forget_Password)
        self.forget_username_edit.setGeometry(QtCore.QRect(240, 40, 346, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.forget_username_edit.setFont(font)
        self.forget_username_edit.setStyleSheet("QLineEdit\n"
"{\n"
"color:rgb(0,0,127);\n"
"}")
        self.forget_username_edit.setClearButtonEnabled(True)
        self.forget_username_edit.setObjectName("forget_username_edit")
        self.forget_verification_code_label = QtWidgets.QLabel(Forget_Password)
        self.forget_verification_code_label.setGeometry(QtCore.QRect(10, 170, 200, 36))
        self.forget_verification_code_label.setObjectName("forget_verification_code_label")
        self.forget_email_edit = QtWidgets.QLineEdit(Forget_Password)
        self.forget_email_edit.setGeometry(QtCore.QRect(240, 105, 346, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.forget_email_edit.setFont(font)
        self.forget_email_edit.setStyleSheet("QLineEdit\n"
"{\n"
"color:rgb(0,0,127);\n"
"}")
        self.forget_email_edit.setClearButtonEnabled(True)
        self.forget_email_edit.setObjectName("forget_email_edit")
        self.forget_verification_code_edit = QtWidgets.QLineEdit(Forget_Password)
        self.forget_verification_code_edit.setGeometry(QtCore.QRect(240, 170, 346, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.forget_verification_code_edit.setFont(font)
        self.forget_verification_code_edit.setStyleSheet("QLineEdit\n"
"{\n"
"color:rgb(0,0,127);\n"
"}")
        self.forget_verification_code_edit.setClearButtonEnabled(True)
        self.forget_verification_code_edit.setObjectName("forget_verification_code_edit")
        self.forget_cancle_btn = QtWidgets.QPushButton(Forget_Password)
        self.forget_cancle_btn.setGeometry(QtCore.QRect(490, 300, 100, 43))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.forget_cancle_btn.setFont(font)
        self.forget_cancle_btn.setStyleSheet("QPushButton\n"
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
        self.forget_cancle_btn.setObjectName("forget_cancle_btn")
        self.forget_email_label = QtWidgets.QLabel(Forget_Password)
        self.forget_email_label.setGeometry(QtCore.QRect(10, 105, 200, 36))
        self.forget_email_label.setObjectName("forget_email_label")
        self.forget_get_verification_btn = QtWidgets.QPushButton(Forget_Password)
        self.forget_get_verification_btn.setGeometry(QtCore.QRect(620, 105, 200, 43))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.forget_get_verification_btn.setFont(font)
        self.forget_get_verification_btn.setStyleSheet("QPushButton\n"
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
        self.forget_get_verification_btn.setObjectName("forget_get_verification_btn")
        self.forget_tooltip_label = QtWidgets.QLabel(Forget_Password)
        self.forget_tooltip_label.setGeometry(QtCore.QRect(210, 235, 600, 45))
        self.forget_tooltip_label.setObjectName("forget_tooltip_label")

        self.retranslateUi(Forget_Password)
        QtCore.QMetaObject.connectSlotsByName(Forget_Password)

    def retranslateUi(self, Forget_Password):
        _translate = QtCore.QCoreApplication.translate
        Forget_Password.setWindowTitle(_translate("Forget_Password", "忘记密码"))
        self.forget_submit_btn.setToolTip(_translate("Forget_Password", "<html><head/><body><p><span style=\" font-size:20pt;\">提交验证信息</span></p></body></html>"))
        self.forget_submit_btn.setText(_translate("Forget_Password", "提交"))
        self.forget_username_label.setText(_translate("Forget_Password", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#00007f;\">用户名</span></p></body></html>"))
        self.forget_verification_code_label.setText(_translate("Forget_Password", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#00007f;\">验证码</span></p></body></html>"))
        self.forget_cancle_btn.setToolTip(_translate("Forget_Password", "<html><head/><body><p><span style=\" font-size:20pt;\">取消验证</span></p></body></html>"))
        self.forget_cancle_btn.setText(_translate("Forget_Password", "取消"))
        self.forget_email_label.setText(_translate("Forget_Password", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#00007f;\">注册邮箱</span></p></body></html>"))
        self.forget_get_verification_btn.setToolTip(_translate("Forget_Password", "<html><head/><body><p><span style=\" font-size:20pt;\">邮箱获取验证码</span></p></body></html>"))
        self.forget_get_verification_btn.setText(_translate("Forget_Password", "获取验证码"))

from background import *
