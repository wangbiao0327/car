# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_dia.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Regist(object):
    def setupUi(self, Regist):
        Regist.setObjectName("Regist")
        Regist.resize(830, 720)
        Regist.setStyleSheet("QDialog\n"
"{\n"
"    background-image:url(:/new/prefix1/picture/water_zhu_heibai.jpg)\n"
"}")
        self.register_email_edit = QtWidgets.QLineEdit(Regist)
        self.register_email_edit.setGeometry(QtCore.QRect(253, 476, 346, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.register_email_edit.setFont(font)
        self.register_email_edit.setStyleSheet("QLineEdit\n"
"{\n"
"color:rgb(0,0,127);\n"
"}")
        self.register_email_edit.setClearButtonEnabled(True)
        self.register_email_edit.setObjectName("register_email_edit")
        self.register_verification_code_edit = QtWidgets.QLineEdit(Regist)
        self.register_verification_code_edit.setGeometry(QtCore.QRect(253, 532, 346, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.register_verification_code_edit.setFont(font)
        self.register_verification_code_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.register_verification_code_edit.setStyleSheet("QLineEdit\n"
"{\n"
"color:rgb(0,0,127);\n"
"}")
        self.register_verification_code_edit.setClearButtonEnabled(True)
        self.register_verification_code_edit.setObjectName("register_verification_code_edit")
        self.register_verification_code_label = QtWidgets.QLabel(Regist)
        self.register_verification_code_label.setGeometry(QtCore.QRect(10, 532, 200, 36))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.register_verification_code_label.setFont(font)
        self.register_verification_code_label.setObjectName("register_verification_code_label")
        self.register_phonenumber_label = QtWidgets.QLabel(Regist)
        self.register_phonenumber_label.setGeometry(QtCore.QRect(10, 196, 200, 38))
        self.register_phonenumber_label.setObjectName("register_phonenumber_label")
        self.register_car_factory_label = QtWidgets.QLabel(Regist)
        self.register_car_factory_label.setGeometry(QtCore.QRect(10, 252, 200, 36))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.register_car_factory_label.setFont(font)
        self.register_car_factory_label.setObjectName("register_car_factory_label")
        self.register_password_agin_edit = QtWidgets.QLineEdit(Regist)
        self.register_password_agin_edit.setGeometry(QtCore.QRect(253, 140, 346, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.register_password_agin_edit.setFont(font)
        self.register_password_agin_edit.setStyleSheet("QLineEdit\n"
"{\n"
"color:rgb(0,0,127);\n"
"}")
        self.register_password_agin_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.register_password_agin_edit.setClearButtonEnabled(True)
        self.register_password_agin_edit.setObjectName("register_password_agin_edit")
        self.register_enter_button = QtWidgets.QPushButton(Regist)
        self.register_enter_button.setGeometry(QtCore.QRect(254, 656, 100, 43))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.register_enter_button.sizePolicy().hasHeightForWidth())
        self.register_enter_button.setSizePolicy(sizePolicy)
        self.register_enter_button.setSizeIncrement(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.register_enter_button.setFont(font)
        self.register_enter_button.setToolTip("")
        self.register_enter_button.setStyleSheet("QPushButton\n"
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
        self.register_enter_button.setObjectName("register_enter_button")
        self.register_car_model_label = QtWidgets.QLabel(Regist)
        self.register_car_model_label.setGeometry(QtCore.QRect(10, 308, 200, 36))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.register_car_model_label.setFont(font)
        self.register_car_model_label.setObjectName("register_car_model_label")
        self.register_car_color_label = QtWidgets.QLabel(Regist)
        self.register_car_color_label.setGeometry(QtCore.QRect(10, 364, 200, 36))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.register_car_color_label.setFont(font)
        self.register_car_color_label.setObjectName("register_car_color_label")
        self.register_car_model_edit = QtWidgets.QLineEdit(Regist)
        self.register_car_model_edit.setGeometry(QtCore.QRect(253, 308, 346, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.register_car_model_edit.setFont(font)
        self.register_car_model_edit.setStyleSheet("QLineEdit\n"
"{\n"
"color:rgb(0,0,127);\n"
"}")
        self.register_car_model_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.register_car_model_edit.setClearButtonEnabled(True)
        self.register_car_model_edit.setObjectName("register_car_model_edit")
        self.register_tooltip_label = QtWidgets.QLabel(Regist)
        self.register_tooltip_label.setGeometry(QtCore.QRect(113, 591, 600, 45))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.register_tooltip_label.setFont(font)
        self.register_tooltip_label.setText("")
        self.register_tooltip_label.setObjectName("register_tooltip_label")
        self.register_password_label = QtWidgets.QLabel(Regist)
        self.register_password_label.setGeometry(QtCore.QRect(10, 84, 200, 38))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.register_password_label.setFont(font)
        self.register_password_label.setObjectName("register_password_label")
        self.register_car_color_edit = QtWidgets.QLineEdit(Regist)
        self.register_car_color_edit.setGeometry(QtCore.QRect(253, 364, 346, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.register_car_color_edit.setFont(font)
        self.register_car_color_edit.setStyleSheet("QLineEdit\n"
"{\n"
"color:rgb(0,0,127);\n"
"}")
        self.register_car_color_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.register_car_color_edit.setClearButtonEnabled(True)
        self.register_car_color_edit.setObjectName("register_car_color_edit")
        self.register_password_edit = QtWidgets.QLineEdit(Regist)
        self.register_password_edit.setGeometry(QtCore.QRect(253, 84, 346, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.register_password_edit.setFont(font)
        self.register_password_edit.setStyleSheet("QLineEdit\n"
"{\n"
"color:rgb(0,0,127);\n"
"}")
        self.register_password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.register_password_edit.setClearButtonEnabled(True)
        self.register_password_edit.setObjectName("register_password_edit")
        self.register_username_label = QtWidgets.QLabel(Regist)
        self.register_username_label.setGeometry(QtCore.QRect(10, 28, 200, 36))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.register_username_label.setFont(font)
        self.register_username_label.setObjectName("register_username_label")
        self.register_phonenumber_edit = QtWidgets.QLineEdit(Regist)
        self.register_phonenumber_edit.setGeometry(QtCore.QRect(253, 196, 346, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.register_phonenumber_edit.setFont(font)
        self.register_phonenumber_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.register_phonenumber_edit.setStyleSheet("QLineEdit\n"
"{\n"
"color:rgb(0,0,127);\n"
"}")
        self.register_phonenumber_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.register_phonenumber_edit.setClearButtonEnabled(True)
        self.register_phonenumber_edit.setObjectName("register_phonenumber_edit")
        self.register_password_agin_label = QtWidgets.QLabel(Regist)
        self.register_password_agin_label.setGeometry(QtCore.QRect(10, 140, 230, 38))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.register_password_agin_label.setFont(font)
        self.register_password_agin_label.setObjectName("register_password_agin_label")
        self.register_cancel_button = QtWidgets.QPushButton(Regist)
        self.register_cancel_button.setGeometry(QtCore.QRect(449, 656, 100, 43))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.register_cancel_button.sizePolicy().hasHeightForWidth())
        self.register_cancel_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.register_cancel_button.setFont(font)
        self.register_cancel_button.setStyleSheet("QPushButton\n"
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
        self.register_cancel_button.setObjectName("register_cancel_button")
        self.register_car_factory_edit = QtWidgets.QLineEdit(Regist)
        self.register_car_factory_edit.setGeometry(QtCore.QRect(253, 252, 346, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.register_car_factory_edit.setFont(font)
        self.register_car_factory_edit.setStyleSheet("QLineEdit\n"
"{\n"
"color:rgb(0,0,127);\n"
"}")
        self.register_car_factory_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.register_car_factory_edit.setClearButtonEnabled(True)
        self.register_car_factory_edit.setObjectName("register_car_factory_edit")
        self.register_get_verification_code_btn = QtWidgets.QPushButton(Regist)
        self.register_get_verification_code_btn.setGeometry(QtCore.QRect(614, 476, 200, 43))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.register_get_verification_code_btn.setFont(font)
        self.register_get_verification_code_btn.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.register_get_verification_code_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.register_get_verification_code_btn.setStyleSheet("QPushButton\n"
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
        self.register_get_verification_code_btn.setObjectName("register_get_verification_code_btn")
        self.register_email_label = QtWidgets.QLabel(Regist)
        self.register_email_label.setGeometry(QtCore.QRect(10, 476, 200, 36))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.register_email_label.setFont(font)
        self.register_email_label.setObjectName("register_email_label")
        self.register_plate_number_edit = QtWidgets.QLineEdit(Regist)
        self.register_plate_number_edit.setGeometry(QtCore.QRect(253, 420, 346, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.register_plate_number_edit.setFont(font)
        self.register_plate_number_edit.setStyleSheet("QLineEdit\n"
"{\n"
"color:rgb(0,0,127);\n"
"}")
        self.register_plate_number_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.register_plate_number_edit.setClearButtonEnabled(True)
        self.register_plate_number_edit.setObjectName("register_plate_number_edit")
        self.register_username_edit = QtWidgets.QLineEdit(Regist)
        self.register_username_edit.setGeometry(QtCore.QRect(253, 28, 346, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.register_username_edit.sizePolicy().hasHeightForWidth())
        self.register_username_edit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.register_username_edit.setFont(font)
        self.register_username_edit.setStyleSheet("QLineEdit\n"
"{\n"
"color:rgb(0,0,127);\n"
"placeholder:\'请输入中文\',\n"
"}")
        self.register_username_edit.setInputMask("")
        self.register_username_edit.setClearButtonEnabled(True)
        self.register_username_edit.setObjectName("register_username_edit")
        self.register_plate_number_label = QtWidgets.QLabel(Regist)
        self.register_plate_number_label.setGeometry(QtCore.QRect(10, 420, 200, 36))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.register_plate_number_label.setFont(font)
        self.register_plate_number_label.setObjectName("register_plate_number_label")

        self.retranslateUi(Regist)
        QtCore.QMetaObject.connectSlotsByName(Regist)

    def retranslateUi(self, Regist):
        _translate = QtCore.QCoreApplication.translate
        Regist.setWindowTitle(_translate("Regist", "欢迎注册爱停车"))
        self.register_verification_code_label.setText(_translate("Regist", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#00007f;\">验 证 码</span></p></body></html>"))
        self.register_phonenumber_label.setText(_translate("Regist", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#00007f;\">手 机 号</span></p></body></html>"))
        self.register_car_factory_label.setText(_translate("Regist", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#00007f;\">汽车厂商</span></p></body></html>"))
        self.register_enter_button.setText(_translate("Regist", "确定"))
        self.register_car_model_label.setText(_translate("Regist", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#00007f;\">车辆型号</span></p></body></html>"))
        self.register_car_color_label.setText(_translate("Regist", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#00007f;\">车辆颜色</span></p></body></html>"))
        self.register_password_label.setText(_translate("Regist", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#00007f;\">密 码</span></p></body></html>"))
        self.register_username_label.setText(_translate("Regist", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#00007f;\">用 户 名</span></p></body></html>"))
        self.register_password_agin_label.setText(_translate("Regist", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#00007f;\">再次输入密码</span></p></body></html>"))
        self.register_cancel_button.setToolTip(_translate("Regist", "提交注册信息"))
        self.register_cancel_button.setText(_translate("Regist", "取消"))
        self.register_get_verification_code_btn.setText(_translate("Regist", "获取验证码"))
        self.register_email_label.setText(_translate("Regist", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#00007f;\">邮 箱</span></p></body></html>"))
        self.register_plate_number_label.setText(_translate("Regist", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#00007f;\">车 牌 号</span></p></body></html>"))

from background import *
