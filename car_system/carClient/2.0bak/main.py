#！user/bin/env python3.7
# coding:utf-8
# author:wanghongzhang
# email:458620786@qq.com
# time: 2018/10/29

import sys
from PyQt5.QtWidgets import QApplication,QDialog
from register_dia import Ui_Regist
from login_dia import Ui_Login
from forget_dia import Ui_Forget_Password
from car_client import *

class Login(Ui_Login):
    def __init__(self, regist, forget_password, car_client):
        super(Login, self).__init__()
        self.regist = regist
        self.forget_password = forget_password
        self.car_client = car_client
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
        result = self.car_client.login(account=user_name, password=pass_word)
        self.login_tooltip_label.setText(result)

    def display(self):
        self.login_login_btn.clicked.connect(self.login_function)
        self.login_regist_btn.clicked.connect(regist.show)

    def click_btn(self):
        self.login_forget_password_btn.clicked.connect(forget_password.show)



class Regist(Ui_Regist):
    def __init__(self, car_client):
        super(Regist, self).__init__()
        self.car_client = car_client
        self.dialog = QDialog()
        self.setupUi(self.dialog)
        self.click_button()

    def show(self):
        self.dialog.show()

    def click_button(self):
        ##关闭注册界面
        self.register_cancel_button.clicked.connect(self.register_close)
        ##启动注册界面
        self.register_enter_button.clicked.connect(self.regist_function)
        ##获取验证码
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
    def __init__(self, car_client):
        super(Forget_Password, self).__init__()
        self.car_client = car_client
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






if __name__ == "__main__":
    app = QApplication(sys.argv)
    car_client = carClient()

    regist = Regist(car_client)
    forget_password = Forget_Password(car_client)
    login = Login(regist, forget_password, car_client)

    # login.login_regist_btn.clicked.connect(regist.show)
    # login.login_forget_password_btn.clicked.connect(forget_password.show)

    sys.exit(app.exec_())













































