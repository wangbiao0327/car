# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'personal_dia.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Personal_information_dialog(object):
    def setupUi(self, Personal_information_dialog):
        Personal_information_dialog.setObjectName("Personal_information_dialog")
        Personal_information_dialog.resize(630, 810)
        Personal_information_dialog.setMaximumSize(QtCore.QSize(630, 810))
        Personal_information_dialog.setStyleSheet("QDialog{\n"
"    \n"
"    background-image: url(:/new/prefix1/picture/back.jpg)\n"
"}")
        self.personal_info_username_edit = QtWidgets.QLineEdit(Personal_information_dialog)
        self.personal_info_username_edit.setGeometry(QtCore.QRect(260, 75, 346, 45))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.personal_info_username_edit.setFont(font)
        self.personal_info_username_edit.setClearButtonEnabled(True)
        self.personal_info_username_edit.setObjectName("personal_info_username_edit")
        self.personal_info_edit_btn = QtWidgets.QPushButton(Personal_information_dialog)
        self.personal_info_edit_btn.setGeometry(QtCore.QRect(490, 20, 100, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.personal_info_edit_btn.setFont(font)
        self.personal_info_edit_btn.setStyleSheet("QPushButton\n"
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
        self.personal_info_edit_btn.setObjectName("personal_info_edit_btn")
        self.personal_info_username_label = QtWidgets.QLabel(Personal_information_dialog)
        self.personal_info_username_label.setGeometry(QtCore.QRect(10, 75, 200, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.personal_info_username_label.setFont(font)
        self.personal_info_username_label.setStyleSheet("QLabel {\n"
"    color:white; \n"
"}\n"
"")
        self.personal_info_username_label.setObjectName("personal_info_username_label")
        self.personal_info_phone_edit = QtWidgets.QLineEdit(Personal_information_dialog)
        self.personal_info_phone_edit.setGeometry(QtCore.QRect(260, 150, 346, 45))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.personal_info_phone_edit.setFont(font)
        self.personal_info_phone_edit.setClearButtonEnabled(True)
        self.personal_info_phone_edit.setObjectName("personal_info_phone_edit")
        self.personal_info_phone_label = QtWidgets.QLabel(Personal_information_dialog)
        self.personal_info_phone_label.setGeometry(QtCore.QRect(10, 150, 200, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.personal_info_phone_label.setFont(font)
        self.personal_info_phone_label.setStyleSheet("QLabel {\n"
"    color:white; \n"
"}\n"
"")
        self.personal_info_phone_label.setObjectName("personal_info_phone_label")
        self.personal_car_factory_edit = QtWidgets.QLineEdit(Personal_information_dialog)
        self.personal_car_factory_edit.setGeometry(QtCore.QRect(260, 225, 346, 45))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.personal_car_factory_edit.setFont(font)
        self.personal_car_factory_edit.setClearButtonEnabled(True)
        self.personal_car_factory_edit.setObjectName("personal_car_factory_edit")
        self.personal_info_car_factory_label = QtWidgets.QLabel(Personal_information_dialog)
        self.personal_info_car_factory_label.setGeometry(QtCore.QRect(10, 225, 200, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.personal_info_car_factory_label.setFont(font)
        self.personal_info_car_factory_label.setStyleSheet("QLabel {\n"
"    color:white; \n"
"}\n"
"")
        self.personal_info_car_factory_label.setObjectName("personal_info_car_factory_label")
        self.personal_car_model_edit = QtWidgets.QLineEdit(Personal_information_dialog)
        self.personal_car_model_edit.setGeometry(QtCore.QRect(260, 300, 346, 45))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.personal_car_model_edit.setFont(font)
        self.personal_car_model_edit.setClearButtonEnabled(True)
        self.personal_car_model_edit.setObjectName("personal_car_model_edit")
        self.personal_info_car_model_label = QtWidgets.QLabel(Personal_information_dialog)
        self.personal_info_car_model_label.setGeometry(QtCore.QRect(10, 300, 200, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.personal_info_car_model_label.setFont(font)
        self.personal_info_car_model_label.setStyleSheet("QLabel {\n"
"    color:white; \n"
"}\n"
"")
        self.personal_info_car_model_label.setObjectName("personal_info_car_model_label")
        self.personal_info_car_color_edit = QtWidgets.QLineEdit(Personal_information_dialog)
        self.personal_info_car_color_edit.setGeometry(QtCore.QRect(260, 375, 346, 45))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.personal_info_car_color_edit.setFont(font)
        self.personal_info_car_color_edit.setClearButtonEnabled(True)
        self.personal_info_car_color_edit.setObjectName("personal_info_car_color_edit")
        self.personal_info_car_color_label = QtWidgets.QLabel(Personal_information_dialog)
        self.personal_info_car_color_label.setGeometry(QtCore.QRect(10, 375, 200, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.personal_info_car_color_label.setFont(font)
        self.personal_info_car_color_label.setStyleSheet("QLabel {\n"
"    color:white; \n"
"}\n"
"")
        self.personal_info_car_color_label.setObjectName("personal_info_car_color_label")
        self.personal_info_plate_edit = QtWidgets.QLineEdit(Personal_information_dialog)
        self.personal_info_plate_edit.setGeometry(QtCore.QRect(260, 450, 346, 45))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.personal_info_plate_edit.setFont(font)
        self.personal_info_plate_edit.setClearButtonEnabled(True)
        self.personal_info_plate_edit.setObjectName("personal_info_plate_edit")
        self.personal_info_plate_label = QtWidgets.QLabel(Personal_information_dialog)
        self.personal_info_plate_label.setGeometry(QtCore.QRect(10, 450, 200, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.personal_info_plate_label.setFont(font)
        self.personal_info_plate_label.setStyleSheet("QLabel {\n"
"    color:white; \n"
"}\n"
"")
        self.personal_info_plate_label.setObjectName("personal_info_plate_label")
        self.personal_info_car_place_label = QtWidgets.QLabel(Personal_information_dialog)
        self.personal_info_car_place_label.setGeometry(QtCore.QRect(10, 525, 200, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.personal_info_car_place_label.setFont(font)
        self.personal_info_car_place_label.setStyleSheet("QLabel {\n"
"    color:white; \n"
"}\n"
"")
        self.personal_info_car_place_label.setObjectName("personal_info_car_place_label")
        self.personal_info_car_place_edit = QtWidgets.QLineEdit(Personal_information_dialog)
        self.personal_info_car_place_edit.setGeometry(QtCore.QRect(260, 525, 346, 45))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.personal_info_car_place_edit.setFont(font)
        self.personal_info_car_place_edit.setClearButtonEnabled(True)
        self.personal_info_car_place_edit.setObjectName("personal_info_car_place_edit")
        self.personal_info_member_edit = QtWidgets.QLineEdit(Personal_information_dialog)
        self.personal_info_member_edit.setGeometry(QtCore.QRect(260, 600, 346, 45))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.personal_info_member_edit.setFont(font)
        self.personal_info_member_edit.setClearButtonEnabled(True)
        self.personal_info_member_edit.setObjectName("personal_info_member_edit")
        self.personal_info_member_label = QtWidgets.QLabel(Personal_information_dialog)
        self.personal_info_member_label.setGeometry(QtCore.QRect(10, 600, 200, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.personal_info_member_label.setFont(font)
        self.personal_info_member_label.setStyleSheet("QLabel {\n"
"    color:white; \n"
"}\n"
"")
        self.personal_info_member_label.setObjectName("personal_info_member_label")
        self.personal_info_submit_btn = QtWidgets.QPushButton(Personal_information_dialog)
        self.personal_info_submit_btn.setGeometry(QtCore.QRect(300, 760, 100, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.personal_info_submit_btn.setFont(font)
        self.personal_info_submit_btn.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(166,166,166);\n"
"color:white;\n"
"border:1px solid rgb(168,168,168);\n"
"background:rgba(0,0,0,0);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"\n"
"background-color:rgba(239,239,239,1);\n"
"color:back;\n"
"background:rgba(166,166,166,1);\n"
"}")
        self.personal_info_submit_btn.setObjectName("personal_info_submit_btn")
        self.personal_info_cancle_btn = QtWidgets.QPushButton(Personal_information_dialog)
        self.personal_info_cancle_btn.setGeometry(QtCore.QRect(450, 760, 100, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.personal_info_cancle_btn.setFont(font)
        self.personal_info_cancle_btn.setStyleSheet("QPushButton\n"
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
        self.personal_info_cancle_btn.setObjectName("personal_info_cancle_btn")
        self.personal_info_email_edit = QtWidgets.QLineEdit(Personal_information_dialog)
        self.personal_info_email_edit.setGeometry(QtCore.QRect(260, 675, 346, 45))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.personal_info_email_edit.setFont(font)
        self.personal_info_email_edit.setClearButtonEnabled(True)
        self.personal_info_email_edit.setObjectName("personal_info_email_edit")
        self.personal_info_email_label = QtWidgets.QLabel(Personal_information_dialog)
        self.personal_info_email_label.setGeometry(QtCore.QRect(10, 675, 200, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.personal_info_email_label.setFont(font)
        self.personal_info_email_label.setStyleSheet("QLabel {\n"
"    color:white; \n"
"}\n"
"")
        self.personal_info_email_label.setObjectName("personal_info_email_label")
        self.personal_info_tooltip_label = QtWidgets.QLabel(Personal_information_dialog)
        self.personal_info_tooltip_label.setGeometry(QtCore.QRect(10, 750, 251, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.personal_info_tooltip_label.setFont(font)
        self.personal_info_tooltip_label.setStyleSheet("QLabel {\n"
"    color:white; \n"
"}\n"
"")
        self.personal_info_tooltip_label.setObjectName("personal_info_tooltip_label")

        self.retranslateUi(Personal_information_dialog)
        QtCore.QMetaObject.connectSlotsByName(Personal_information_dialog)

    def retranslateUi(self, Personal_information_dialog):
        _translate = QtCore.QCoreApplication.translate
        Personal_information_dialog.setWindowTitle(_translate("Personal_information_dialog", "个人资料"))
        self.personal_info_edit_btn.setToolTip(_translate("Personal_information_dialog", "<html><head/><body><p>可更改联系电话</p></body></html>"))
        self.personal_info_edit_btn.setText(_translate("Personal_information_dialog", "编辑"))
        self.personal_info_username_label.setText(_translate("Personal_information_dialog", "用户名"))
        self.personal_info_phone_label.setText(_translate("Personal_information_dialog", "联系电话"))
        self.personal_info_car_factory_label.setText(_translate("Personal_information_dialog", "汽车厂家"))
        self.personal_info_car_model_label.setText(_translate("Personal_information_dialog", "车辆型号"))
        self.personal_info_car_color_label.setText(_translate("Personal_information_dialog", "车辆颜色"))
        self.personal_info_plate_label.setText(_translate("Personal_information_dialog", "车牌号"))
        self.personal_info_car_place_label.setText(_translate("Personal_information_dialog", "车位"))
        self.personal_info_member_label.setText(_translate("Personal_information_dialog", "专属会员"))
        self.personal_info_submit_btn.setToolTip(_translate("Personal_information_dialog", "提交修改信息"))
        self.personal_info_submit_btn.setText(_translate("Personal_information_dialog", "提交"))
        self.personal_info_cancle_btn.setToolTip(_translate("Personal_information_dialog", "取消编辑"))
        self.personal_info_cancle_btn.setText(_translate("Personal_information_dialog", "取消"))
        self.personal_info_email_label.setText(_translate("Personal_information_dialog", "邮箱"))
        self.personal_info_tooltip_label.setText(_translate("Personal_information_dialog", "<html><head/><body><p><span style=\" color:#00aaff;\">修改成功，修改成功，修改成功</span></p></body></html>"))

from background import *
