# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from car_client import *
from messageAff import *

class Ui_Register(object):
    def __init__(self):
        super().__init__()
        self.widget = QWidget()
        self.car_client = carClient()
        self.setupUi(self.widget)
        self.widget.show()
        self.show()
        

    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.setEnabled(True)
        Register.resize(830, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Register.sizePolicy().hasHeightForWidth())
        Register.setSizePolicy(sizePolicy)
        Register.setMinimumSize(QtCore.QSize(200, 32))
        Register.setMaximumSize(QtCore.QSize(830, 720))
        Register.setSizeIncrement(QtCore.QSize(200, 32))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(26)
        Register.setFont(font)
        self.register_username_edit = QtWidgets.QLineEdit(Register)
        self.register_username_edit.setGeometry(QtCore.QRect(249, 22, 346, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.register_username_edit.sizePolicy().hasHeightForWidth())
        self.register_username_edit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.register_username_edit.setFont(font)
        self.register_username_edit.setStyleSheet("")
        self.register_username_edit.setInputMask("")
        self.register_username_edit.setClearButtonEnabled(True)
        self.register_username_edit.setObjectName("register_username_edit")
        self.register_password_edit = QtWidgets.QLineEdit(Register)
        self.register_password_edit.setGeometry(QtCore.QRect(249, 78, 346, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.register_password_edit.setFont(font)
        self.register_password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.register_password_edit.setClearButtonEnabled(True)
        self.register_password_edit.setObjectName("register_password_edit")
        self.register_username_label = QtWidgets.QLabel(Register)
        self.register_username_label.setGeometry(QtCore.QRect(6, 22, 200, 36))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.register_username_label.setFont(font)
        self.register_username_label.setObjectName("register_username_label")
        self.register_password_label = QtWidgets.QLabel(Register)
        self.register_password_label.setGeometry(QtCore.QRect(6, 78, 200, 38))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.register_password_label.setFont(font)
        self.register_password_label.setObjectName("register_password_label")
        self.register_car_factory_edit = QtWidgets.QLineEdit(Register)
        self.register_car_factory_edit.setGeometry(QtCore.QRect(249, 246, 346, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.register_car_factory_edit.setFont(font)
        self.register_car_factory_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.register_car_factory_edit.setClearButtonEnabled(True)
        self.register_car_factory_edit.setObjectName("register_car_factory_edit")
        self.register_car_model_edit = QtWidgets.QLineEdit(Register)
        self.register_car_model_edit.setGeometry(QtCore.QRect(249, 302, 346, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.register_car_model_edit.setFont(font)
        self.register_car_model_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.register_car_model_edit.setClearButtonEnabled(True)
        self.register_car_model_edit.setObjectName("register_car_model_edit")
        self.register_phonenumber_label = QtWidgets.QLabel(Register)
        self.register_phonenumber_label.setGeometry(QtCore.QRect(6, 190, 200, 38))
        self.register_phonenumber_label.setObjectName("register_phonenumber_label")
        self.register_password_agin_edit = QtWidgets.QLineEdit(Register)
        self.register_password_agin_edit.setGeometry(QtCore.QRect(249, 134, 346, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.register_password_agin_edit.setFont(font)
        self.register_password_agin_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.register_password_agin_edit.setClearButtonEnabled(True)
        self.register_password_agin_edit.setObjectName("register_password_agin_edit")
        self.register_car_model_label = QtWidgets.QLabel(Register)
        self.register_car_model_label.setGeometry(QtCore.QRect(6, 302, 200, 36))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.register_car_model_label.setFont(font)
        self.register_car_model_label.setObjectName("register_car_model_label")
        self.register_phonenumber_edit = QtWidgets.QLineEdit(Register)
        self.register_phonenumber_edit.setGeometry(QtCore.QRect(249, 190, 346, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.register_phonenumber_edit.setFont(font)
        self.register_phonenumber_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.register_phonenumber_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.register_phonenumber_edit.setClearButtonEnabled(True)
        self.register_phonenumber_edit.setObjectName("register_phonenumber_edit")
        self.register_car_color_label = QtWidgets.QLabel(Register)
        self.register_car_color_label.setGeometry(QtCore.QRect(6, 358, 200, 36))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.register_car_color_label.setFont(font)
        self.register_car_color_label.setObjectName("register_car_color_label")
        self.register_car_color_edit = QtWidgets.QLineEdit(Register)
        self.register_car_color_edit.setGeometry(QtCore.QRect(249, 358, 346, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.register_car_color_edit.setFont(font)
        self.register_car_color_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.register_car_color_edit.setClearButtonEnabled(True)
        self.register_car_color_edit.setObjectName("register_car_color_edit")
        self.register_plate_number_label = QtWidgets.QLabel(Register)
        self.register_plate_number_label.setGeometry(QtCore.QRect(6, 414, 200, 36))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.register_plate_number_label.setFont(font)
        self.register_plate_number_label.setObjectName("register_plate_number_label")
        self.register_plate_number_edit = QtWidgets.QLineEdit(Register)
        self.register_plate_number_edit.setGeometry(QtCore.QRect(249, 414, 346, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.register_plate_number_edit.setFont(font)
        self.register_plate_number_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.register_plate_number_edit.setClearButtonEnabled(True)
        self.register_plate_number_edit.setObjectName("register_plate_number_edit")
        self.register_email_label = QtWidgets.QLabel(Register)
        self.register_email_label.setGeometry(QtCore.QRect(6, 470, 200, 36))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.register_email_label.setFont(font)
        self.register_email_label.setObjectName("register_email_label")
        self.register_password_agin_label = QtWidgets.QLabel(Register)
        self.register_password_agin_label.setGeometry(QtCore.QRect(6, 134, 230, 38))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.register_password_agin_label.setFont(font)
        self.register_password_agin_label.setObjectName("register_password_agin_label")
        self.register_car_factory_label = QtWidgets.QLabel(Register)
        self.register_car_factory_label.setGeometry(QtCore.QRect(6, 246, 200, 36))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.register_car_factory_label.setFont(font)
        self.register_car_factory_label.setObjectName("register_car_factory_label")
        self.register_email_edit = QtWidgets.QLineEdit(Register)
        self.register_email_edit.setGeometry(QtCore.QRect(249, 470, 346, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.register_email_edit.setFont(font)
        self.register_email_edit.setClearButtonEnabled(True)
        self.register_email_edit.setObjectName("register_email_edit")
        self.register_verification_code_edit = QtWidgets.QLineEdit(Register)
        self.register_verification_code_edit.setGeometry(QtCore.QRect(249, 526, 346, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.register_verification_code_edit.setFont(font)
        self.register_verification_code_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.register_verification_code_edit.setClearButtonEnabled(True)
        self.register_verification_code_edit.setObjectName("register_verification_code_edit")
        self.register_verification_code_label = QtWidgets.QLabel(Register)
        self.register_verification_code_label.setGeometry(QtCore.QRect(6, 526, 200, 36))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.register_verification_code_label.setFont(font)
        self.register_verification_code_label.setObjectName("register_verification_code_label")
        self.register_cancel_button = QtWidgets.QPushButton(Register)

        ##关闭注册界面
        self.register_cancel_button.clicked.connect(self.register_close)

        self.register_cancel_button.setGeometry(QtCore.QRect(445, 650, 100, 43))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.register_cancel_button.sizePolicy().hasHeightForWidth())
        self.register_cancel_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.register_cancel_button.setFont(font)
        self.register_cancel_button.setObjectName("register_cancel_button")
        self.register_enter_button = QtWidgets.QPushButton(Register)

        ##
        self.register_enter_button.clicked.connect(self.regist_function)

        self.register_enter_button.setGeometry(QtCore.QRect(250, 650, 100, 43))
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
        self.register_enter_button.setObjectName("register_enter_button")
        self.register_get_verification_code_btn = QtWidgets.QPushButton(Register)
        ##
        self.register_get_verification_code_btn.clicked.connect(self.send_email)

        self.register_get_verification_code_btn.setGeometry(QtCore.QRect(610, 470, 200, 43))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.register_get_verification_code_btn.setFont(font)
        self.register_get_verification_code_btn.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.register_get_verification_code_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.register_get_verification_code_btn.setObjectName("register_get_verification_code_btn")
        self.register_tooltip_label = QtWidgets.QLabel(Register)
        self.register_tooltip_label.setGeometry(QtCore.QRect(109, 585, 600, 45))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.register_tooltip_label.setFont(font)
        self.register_tooltip_label.setText("")
        self.register_tooltip_label.setObjectName("register_tooltip_label")

        self.retranslateUi(Register)

        

        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "欢迎注册"))
        self.register_username_label.setText(_translate("Register", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">用 户 名</span></p></body></html>"))
        self.register_password_label.setText(_translate("Register", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">密 码</span></p></body></html>"))
        self.register_phonenumber_label.setText(_translate("Register", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">手 机 号</span></p></body></html>"))
        self.register_car_model_label.setText(_translate("Register", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">车辆型号</span></p></body></html>"))
        self.register_car_color_label.setText(_translate("Register", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">车辆颜色</span></p></body></html>"))
        self.register_plate_number_label.setText(_translate("Register", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">车 牌 号</span></p></body></html>"))
        self.register_email_label.setText(_translate("Register", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">邮 箱</span></p></body></html>"))
        self.register_password_agin_label.setText(_translate("Register", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">再次输入密码</span></p></body></html>"))
        self.register_car_factory_label.setText(_translate("Register", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">汽车厂商</span></p></body></html>"))
        self.register_verification_code_label.setText(_translate("Register", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">验 证 码</span></p></body></html>"))
        self.register_cancel_button.setToolTip(_translate("Register", "提交注册信息"))
        self.register_cancel_button.setText(_translate("Register", "取消"))
        self.register_enter_button.setText(_translate("Register", "确定"))
        self.register_get_verification_code_btn.setText(_translate("Register", "获取验证码"))
        


    def regist_function(self):
        self.register_tooltip_label.setText('')
        name = self.register_username_edit.text()
        password = self.register_password_edit.text()
        password_agin = self.register_password_agin_edit.text()
        phone_number = self.register_phonenumber_edit.text()
        car_factory = self.register_car_factory_edit.text()
        car_model = self.register_car_model_edit.text()
        car_color = self.register_car_color_edit.text()
        car_plate_number = self.register_plate_number_edit.text()
        email = self.register_email_edit.text()
        verification_code = self.register_verification_code_edit.text()

        L = [name, password, password_agin, phone_number, car_factory, car_model,
              car_color, car_plate_number, email, verification_code]
        print(L)
        login_result = self.car_client.regist(L)

        self.register_tooltip_label.setText(login_result)
        

    def register_close(self):
        self.widget.close()

    def send_email(self):
        my_email = self.register_email_edit.text()
        self.car_client.send_email(my_email)



        
        



if __name__ == "__main__":

    app = QApplication(sys.argv)
    new = Ui_Register()
    sys.exit(app.exec_())
