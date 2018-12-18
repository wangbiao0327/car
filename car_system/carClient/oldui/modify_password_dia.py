# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modify_password_dia.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Modify_password_dialog(object):
    def setupUi(self, Modify_password_dialog):
        Modify_password_dialog.setObjectName("Modify_password_dialog")
        Modify_password_dialog.resize(600, 400)
        self.modify_nsername_edit = QtWidgets.QLineEdit(Modify_password_dialog)
        self.modify_nsername_edit.setGeometry(QtCore.QRect(230, 40, 346, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.modify_nsername_edit.setFont(font)
        self.modify_nsername_edit.setStyleSheet("QLineEdit{\n"
"    border:1px solid balck;\n"
"}")
        self.modify_nsername_edit.setObjectName("modify_nsername_edit")
        self.modify_password_label = QtWidgets.QLabel(Modify_password_dialog)
        self.modify_password_label.setGeometry(QtCore.QRect(10, 40, 120, 36))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.modify_password_label.setFont(font)
        self.modify_password_label.setObjectName("modify_password_label")
        self.modify_password_tooltip_label = QtWidgets.QLabel(Modify_password_dialog)
        self.modify_password_tooltip_label.setGeometry(QtCore.QRect(10, 250, 520, 36))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.modify_password_tooltip_label.setFont(font)
        self.modify_password_tooltip_label.setObjectName("modify_password_tooltip_label")
        self.modify_password_again__label = QtWidgets.QLabel(Modify_password_dialog)
        self.modify_password_again__label.setGeometry(QtCore.QRect(10, 120, 200, 36))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.modify_password_again__label.setFont(font)
        self.modify_password_again__label.setObjectName("modify_password_again__label")
        self.modify_nsername_edit_2 = QtWidgets.QLineEdit(Modify_password_dialog)
        self.modify_nsername_edit_2.setGeometry(QtCore.QRect(230, 120, 346, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.modify_nsername_edit_2.setFont(font)
        self.modify_nsername_edit_2.setStyleSheet("QLineEdit{\n"
"    border:1px solid balck;\n"
"}")
        self.modify_nsername_edit_2.setObjectName("modify_nsername_edit_2")
        self.modify_password_cancle_btn = QtWidgets.QPushButton(Modify_password_dialog)
        self.modify_password_cancle_btn.setGeometry(QtCore.QRect(400, 320, 100, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.modify_password_cancle_btn.setFont(font)
        self.modify_password_cancle_btn.setStyleSheet("QPushButton{\n"
"    background-color:rgba(170,119,11,1);\n"
"    border:1px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(170,119,11,0.5);\n"
"    color:white;\n"
"}")
        self.modify_password_cancle_btn.setObjectName("modify_password_cancle_btn")
        self.modify_password_enter_btn = QtWidgets.QPushButton(Modify_password_dialog)
        self.modify_password_enter_btn.setGeometry(QtCore.QRect(230, 320, 100, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.modify_password_enter_btn.setFont(font)
        self.modify_password_enter_btn.setStyleSheet("QPushButton{\n"
"    background-color:rgba(170,119,11,1);\n"
"    border:1px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(170,119,11,0.5);\n"
"    color:white;\n"
"}\n"
"")
        self.modify_password_enter_btn.setObjectName("modify_password_enter_btn")
        self.modify_nsername_edit_3 = QtWidgets.QLineEdit(Modify_password_dialog)
        self.modify_nsername_edit_3.setGeometry(QtCore.QRect(230, 190, 346, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.modify_nsername_edit_3.setFont(font)
        self.modify_nsername_edit_3.setStyleSheet("QLineEdit{\n"
"    border:1px solid balck;\n"
"}")
        self.modify_nsername_edit_3.setObjectName("modify_nsername_edit_3")
        self.modify_password_get_verification_btn = QtWidgets.QPushButton(Modify_password_dialog)
        self.modify_password_get_verification_btn.setGeometry(QtCore.QRect(10, 190, 200, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.modify_password_get_verification_btn.setFont(font)
        self.modify_password_get_verification_btn.setStyleSheet("QPushButton{\n"
"    background-color:rgba(170,119,11,1);\n"
"    border:1px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(170,119,11,0.5);\n"
"    color:white;\n"
"}\n"
"")
        self.modify_password_get_verification_btn.setObjectName("modify_password_get_verification_btn")

        self.retranslateUi(Modify_password_dialog)
        QtCore.QMetaObject.connectSlotsByName(Modify_password_dialog)

    def retranslateUi(self, Modify_password_dialog):
        _translate = QtCore.QCoreApplication.translate
        Modify_password_dialog.setWindowTitle(_translate("Modify_password_dialog", "Dialog"))
        self.modify_password_label.setText(_translate("Modify_password_dialog", "新密码"))
        self.modify_password_tooltip_label.setText(_translate("Modify_password_dialog", "<html><head/><body><p><span style=\" color:#00aaff;\">请按正确的格式输入，允许使用字母、数字</span></p></body></html>"))
        self.modify_password_again__label.setText(_translate("Modify_password_dialog", "再次输入密码"))
        self.modify_password_cancle_btn.setText(_translate("Modify_password_dialog", "取消"))
        self.modify_password_enter_btn.setText(_translate("Modify_password_dialog", "确定"))
        self.modify_password_get_verification_btn.setText(_translate("Modify_password_dialog", "获取邮箱验证码"))

