#！user/bin/env python3.7
# coding:utf-8
# author:wanghongzhang
# email:458620786@qq.com
# time: 2018/10/30

import sys
import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from user_ui_main import Ui_User_UI
from personal_dia import Ui_Personal_information_dialog
from history_dia import Ui_History_stop
from modify_username_dia import Ui_Modify_username_dia
from modify_password_dia import Ui_Modify_password_dialog
from xialatest import Ui_Dialog

class Main(Ui_User_UI):
    def __init__(self, personal, history, modify_uname, modify_password):
        super(Main, self).__init__()
        self.personal = personal
        self.history = history
        self.modify_uname = modify_uname
        self.modify_password = modify_password
        self.mainwindow = QMainWindow()
        self.setupUi(self.mainwindow)
        self.mainwindow.show()
        self.update_time()
        self.click()

    def update_time(self):
        date = datetime.date.today()
        self.calendar_widget.setSelectedDate(QtCore.QDate(int(date.year),
                                               int(date.month), int(date.day)))

    def click(self):
        self.personal_information_btn.clicked.connect(
            self.personal_function)
        self.stop_car_history_btn.clicked.connect(
            self.history_function)
        self.modify_username_btn.clicked.connect(
            self.modify_username_function)
        self.modify_password_btn.clicked.connect(
            self.modify_password_function)

    def personal_function(self):
        self.personal.show()

    def history_function(self):
        self.history.show()

    def modify_username_function(self):
        self.modify_uname.show()

    def modify_password_function(self):
        self.modify_password.show()


class Personal(Ui_Personal_information_dialog):
    def __init__(self):
        super(Personal, self).__init__()
        self.dialog = QDialog()
        self.setupUi(self.dialog)
        self.click()

    def show(self):
        self.dialog.show()

    def click(self):
        self.personal_info_cancle_btn.clicked.connect(self.close)
        self.personal_info_username_edit.setEnabled(False)

    def close(self):
        self.dialog.close()


class History(Ui_History_stop):
    def __init__(self):
        super(History, self).__init__()
        self.dialog = QDialog()
        self.setupUi(self.dialog)


    def show(self):
        self.dialog.show()



class Modify_username(Ui_Modify_username_dia):
    def __init__(self):
        super(Modify_username, self).__init__()
        self.dialog = QDialog()
        self.setupUi(self.dialog)
        self.click()

    def show(self):
        self.dialog.show()

    def click(self):
        self.modify_cancle_btn.clicked.connect(self.close)

    def close(self):
        self.dialog.close()

class Modify_password(Ui_Modify_password_dialog):
    def __init__(self):
        self.dialog = QDialog()
        self.setupUi(self.dialog)
        self.click()

    def show(self):
        self.dialog.show()

    def click(self):
        self.modify_password_cancle_btn.clicked.connect(self.close)

    def close(self):
        self.dialog.close()

class Xiala(Ui_Dialog):
    def __init__(self):
        self.dialog = QDialog()
        self.setupUi(self.dialog)
        self.dialog.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    #创建个人资料窗口
    personal = Personal()
    #创建历史纪录窗口
    history = History()
    #创建修改用户名窗口
    modify_uname = Modify_username()
    #创建修改密码窗口
    modify_password = Modify_password()
    # 创建主界面
    main = Main(personal, history, modify_uname, modify_password)
    #创建下拉菜单
    # xiala = Xiala()
    sys.exit(app.exec_())

























