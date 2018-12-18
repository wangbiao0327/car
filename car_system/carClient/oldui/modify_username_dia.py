# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modify_username_dia.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Modify_username_dia(object):
    def setupUi(self, Modify_username_dia):
        Modify_username_dia.setObjectName("Modify_username_dia")
        Modify_username_dia.resize(571, 240)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/picture/yeah.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Modify_username_dia.setWindowIcon(icon)
        Modify_username_dia.setStyleSheet("QDialog{\n"
"    background-color:rgba(126,194,66,1);\n"
"}")
        self.modify_enter_btn = QtWidgets.QPushButton(Modify_username_dia)
        self.modify_enter_btn.setGeometry(QtCore.QRect(260, 160, 100, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.modify_enter_btn.setFont(font)
        self.modify_enter_btn.setStyleSheet("QPushButton{\n"
"    background-color:rgba(170,119,11,1);\n"
"    border:1px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(170,119,11,0.5);\n"
"    color:white;\n"
"}\n"
"")
        self.modify_enter_btn.setObjectName("modify_enter_btn")
        self.modify_nsername_edit = QtWidgets.QLineEdit(Modify_username_dia)
        self.modify_nsername_edit.setGeometry(QtCore.QRect(200, 40, 346, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.modify_nsername_edit.setFont(font)
        self.modify_nsername_edit.setStyleSheet("QLineEdit{\n"
"    border:1px solid balck;\n"
"}")
        self.modify_nsername_edit.setObjectName("modify_nsername_edit")
        self.modify_nsername_label = QtWidgets.QLabel(Modify_username_dia)
        self.modify_nsername_label.setGeometry(QtCore.QRect(20, 40, 120, 36))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.modify_nsername_label.setFont(font)
        self.modify_nsername_label.setObjectName("modify_nsername_label")
        self.modify_cancle_btn = QtWidgets.QPushButton(Modify_username_dia)
        self.modify_cancle_btn.setGeometry(QtCore.QRect(430, 160, 100, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.modify_cancle_btn.setFont(font)
        self.modify_cancle_btn.setStyleSheet("QPushButton{\n"
"    background-color:rgba(170,119,11,1);\n"
"    border:1px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(170,119,11,0.5);\n"
"    color:white;\n"
"}")
        self.modify_cancle_btn.setObjectName("modify_cancle_btn")
        self.modify_tooltip_label = QtWidgets.QLabel(Modify_username_dia)
        self.modify_tooltip_label.setGeometry(QtCore.QRect(40, 100, 471, 36))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.modify_tooltip_label.setFont(font)
        self.modify_tooltip_label.setObjectName("modify_tooltip_label")

        self.retranslateUi(Modify_username_dia)
        QtCore.QMetaObject.connectSlotsByName(Modify_username_dia)

    def retranslateUi(self, Modify_username_dia):
        _translate = QtCore.QCoreApplication.translate
        Modify_username_dia.setWindowTitle(_translate("Modify_username_dia", "修改用户名"))
        self.modify_enter_btn.setText(_translate("Modify_username_dia", "确定"))
        self.modify_nsername_label.setText(_translate("Modify_username_dia", "新用户名"))
        self.modify_cancle_btn.setText(_translate("Modify_username_dia", "取消"))
        self.modify_tooltip_label.setText(_translate("Modify_username_dia", "请按正确的格式输入，允许使用中文、字母、数字"))

from backgrounImage import *
