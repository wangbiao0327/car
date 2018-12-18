#！user/bin/env python3.7
# coding:utf-8
# author:wanghongzhang
# email:458620786@qq.com
# time: 2018/10/29

import sys
import datetime
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic.properties import QtCore
from PyQt5 import QtCore, QtGui, QtWidgets

from register_dia import Ui_Regist
from login_dia import Ui_Login
from forget_dia import Ui_Forget_Password

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from user_ui_main import Ui_User_UI
from personal_dia import Ui_Personal_information_dialog
from history_dia import Ui_History_stop
from modify_username_dia import Ui_Modify_username_dia
from modify_password_dia import Ui_Modify_password_dialog
from xialatest import Ui_Dialog

class Login(Ui_Login):
    def __init__(self, main, regist, forget_password):
        super(Login, self).__init__()
        self.main = main
        self.regist = regist
        self.forget_password = forget_password
        self.dialog = QDialog()
        self.setupUi(self.dialog)
        self.dialog.show()
        self.display()
        self.click_btn()

    def login_function(self):
        user_name = self.login_username_lineEdit.text()
        pass_word = self.login_password_lineEdit.text()
        L = [user_name, pass_word]
        print(L)
        # result = self.car_client.login(account=user_name, password=pass_word)
        # self.login_tooltip_label.setText(result)
        self.main.show()
        self.dialog.close()

    def display(self):
        self.login_login_btn.clicked.connect(self.login_function)
        self.login_regist_btn.clicked.connect(self.regist.show)

    def click_btn(self):
        self.login_forget_password_btn.clicked.connect(self.forget_password.show)



class Regist(Ui_Regist):
    def __init__(self):
        super(Regist, self).__init__()
        self.dialog = QDialog()
        self.setupUi(self.dialog)
        self.click_button()

    def show(self):
        self.dialog.show()

    def click_button(self):
        ##关闭注册界面
        self.register_cancel_button.clicked.connect(self.register_close)
        ##
        self.register_enter_button.clicked.connect(self.regist_function)
        ##
        self.register_get_verification_code_btn.clicked.connect(self.send_email)

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
        self.dialog.close()

    def send_email(self):
        my_email = self.register_email_edit.text()
        self.car_client.send_email(my_email)



class Forget_Password(Ui_Forget_Password):
    def __init__(self):
        super(Forget_Password, self).__init__()
        self.dialog = QDialog()
        self.setupUi(self.dialog)
        self.click_button()

    def show(self):
        self.dialog.show()

    def click_button(self):
        ##
        self.forget_cancle_btn.clicked.connect(self.close)
        self.forget_get_verification_btn.clicked.connect(self.get_verification_code)


    def close(self):
        self.dialog.close()

    def get_verification_code(self):

        login_account = self.forget_username_edit.text()
        login_email = self.forget_email_edit.text()

        # 判断邮箱输入且格式正确
        if login_email:

            self.forget_tooltip_label.setText("")
            judge_result = self.judge_email(login_email)

            if judge_result:
                self.forget_tooltip_label.setText("验证码已发送，请耐心等待...")

            else:
                self.forget_tooltip_label.setText("请输入合法邮箱")

        else:
            self.forget_tooltip_label.setText("邮箱不能为空")  # 没有输入注册邮箱提示邮箱不能为空

        # 账户传入，调用client对象
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

#=======================================================================
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
        self.click()
        self.update_time()

    def show(self):
        self.mainwindow.show()

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























if __name__ == "__main__":
    app = QApplication(sys.argv)


    # 创建个人资料窗口
    personal = Personal()
    # 创建历史纪录窗口
    history = History()
    # 创建修改用户名窗口
    modify_uname = Modify_username()
    # 创建修改密码窗口
    modify_password = Modify_password()

    # 创建主界面
    main = Main(personal, history, modify_uname, modify_password)

    regist = Regist()
    forget_password = Forget_Password()
    login = Login(main, regist, forget_password)

    sys.exit(app.exec_())













































