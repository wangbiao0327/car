#！user/bin/env python3.7
# coding:utf-8
# author:wanghongzhang
# email:458620786@qq.com
# time: 2018/10/29

import sys
import datetime
from login_dia import Ui_Login
from register_dia import Ui_Regist
from forget_dia import Ui_Forget_Password
from PyQt5.uic.properties import QtCore
from PyQt5 import QtCore, QtGui, QtWidgets
from personal_dia import Ui_Personal_information_dialog
from history_dia import Ui_History_stop
from modify_username_dia import Ui_Modify_username_dia
from modify_password_dia import Ui_Modify_password_dialog
from user_ui_main import Ui_User_UI
from xialatest import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

from car_client import *
from messageAff import user_message


class Login(Ui_Login):
    def __init__(self, main, regist, forget_password, car_client):
        super(Login, self).__init__()
        self.main = main
        self.regist = regist
        self.forget_password = forget_password
        self.car_client = car_client

        self.dialog = QDialog()
        self.setupUi(self.dialog)
        self.dialog.show()

        self.display()
       

    def display(self):
        self.login_login_btn.clicked.connect(self.login_function)
        self.login_regist_btn.clicked.connect(self.regist.show)
        self.login_forget_password_btn.clicked.connect(self.forget_password.show)

    def login_function(self):
        user_name = self.login_username_lineEdit.text()
        pass_word = self.login_password_lineEdit.text()
        L = [user_name, pass_word]
        # print("输入的用户名和密码",L)
        result = self.car_client.Login(user_name, pass_word)
        # self.login_tooltip_label.setText(result)
        if result[0]:
            self.dialog.close()
            self.show_main(user_name)
        else:
            self.login_tooltip_label.setText(result[1]+'登录失败')
            return

    def show_main(self, user_name):
        self.main.show(user_name)



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
        ##点击提交，进行注册
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
        verification_code = self.register_verification_code_edit.text().strip()

        
        L = [name, password, password_agin, phone_number, car_factory, car_model,
             car_color, car_plate_number, email, verification_code]
        # print(L)
        login_result = self.car_client.Register(name, password, phone_number, car_factory, car_model,car_color, car_plate_number, email)
        # print("注册结果",login_result)
        if login_result[0]:
            self.register_tooltip_label.setText('注册成功,现在去登录吧！')
            time.sleep(3)
            self.dialog.close()
      
    def register_close(self):
        self.dialog.close()

    def send_email(self):
        my_email = self.register_email_edit.text()
        
        self.email_code = self.car_client.send_email(my_email)
      


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
        # print(self.forget_verification_code)

        try:
            if type(int(self.forget_verification_code)) is not int:
                self.forget_tooltip_label.setText("您输入的账号不存在，请检查后再输入")
        except ValueError:
            self.forget_tooltip_label.setText(self.forget_verification_code)

    def judge_email(self, login_email):
        import re

        pettern = r"\w+@\w+\.[a-z]+"
        L_result = re.findall(pettern, login_email)
        # print(L_result)
        if L_result:
            if len(login_email) == len(L_result[0]):
                return True

        return False

#=======================================================================
class Main(Ui_User_UI):
    def __init__(self, personal, history, modify_uname, modify_password,car_client):
        super(Main, self).__init__()
        self.personal = personal
        self.history = history
        self.modify_uname = modify_uname
        self.modify_password = modify_password
        self.car_client = car_client
        self.mainwindow = QMainWindow()
        self.setupUi(self.mainwindow)
        self.click()
        self.update_time()

    def update_time(self):
        date = datetime.date.today()
        self.calendar_widget.setSelectedDate(QtCore.QDate(int(date.year),
                                               int(date.month), int(date.day)))


    def show(self, user_name):
        self.user_name = user_name
        html = "<html><head/><body><p><span style=\" color:#00aaff;\">"+self.user_name+"</span></p></body></html>"
        self.account_name_label.setText(html)
        self.mainwindow.show()
        # self.personal.information(self.user_name)


    def user_logout(self):
        self.car_client.User_quit(self.user_name)
        self.mainwindow.close()

    def click(self):
        self.personal_information_btn.clicked.connect(
            self.personal_function)

        self.stop_car_history_btn.clicked.connect(
            self.history_function)

        self.modify_username_btn.clicked.connect(
            self.modify_username_function)
        
        self.modify_password_btn.clicked.connect(
            self.modify_password_function)
        self.logout_btn.clicked.connect(self.user_logout)


    def personal_function(self):
        self.personal.show(self.user_name)

    def history_function(self):
        self.history.show(self.user_name)

    def modify_username_function(self):
        self.modify_uname.show(self.user_name)

    def modify_password_function(self):
        self.modify_password.show(self.user_name)


class Personal(Ui_Personal_information_dialog):
    def __init__(self, car_client):
        super(Personal, self).__init__()
        self.car_client = car_client
        self.dialog = QDialog()
        self.setupUi(self.dialog)
        self.click()

    def show(self, user_name):
        self.user_name = user_name
        self.dialog.show()
        self.test()
        self.personal_info_username_edit.setEnabled(False)
        self.personal_info_phone_edit.setEnabled(False)
        self.personal_car_factory_edit.setEnabled(False)
        self.personal_car_model_edit.setEnabled(False)
        self.personal_info_car_color_edit.setEnabled(False)
        self.personal_info_plate_edit.setEnabled(False)
        self.personal_info_car_place_edit.setEnabled(False)
        self.personal_info_member_edit.setEnabled(False)
        self.personal_info_email_edit.setEnabled(False)



    def click(self):
        self.personal_info_cancle_btn.clicked.connect(self.close)
        self.personal_info_edit_btn.clicked.connect(self.edit_info)
        self.personal_info_submit_btn.clicked.connect(self.personal_informatin_submit)

    def close(self):
        self.dialog.close()

    def  information(self, user_name):
        self.user_name = user_name
        

    def test(self):
        try:
            self.result = self.car_client.Personal_information_display(self.user_name)
        except Exception as e:
            return
        if self.result[0] == False:
            return
        self.history_lists = self.result
        self.personal_info_username_edit.setText(self.result[0])
        self.personal_info_phone_edit.setText(self.result[1])
        self.personal_car_factory_edit.setText(self.result[2])
        self.personal_car_model_edit.setText(self.result[3])
        self.personal_info_car_color_edit.setText(self.result[4])
        self.personal_info_plate_edit.setText(self.result[5])
        if self.result[7] == 'False':
            self.personal_info_car_place_edit.setText(self.result[6])
            self.personal_info_member_edit.setText(self.result[7])
        else:
            self.personal_info_car_place_edit.setText('不是会员没有专属车位')
            self.personal_info_member_edit.setText('不是会员')
        self.personal_info_email_edit.setText(self.result[8])
        self.car_client.User_quit(self.user_name)

        #此函数用于编辑按钮设置信息编辑状态
    def edit_info(self):
        if self.personal_info_username_edit.isEnabled():
            self.personal_info_username_edit.setEnabled(False)
            self.personal_info_phone_edit.setEnabled(False)
            self.personal_car_factory_edit.setEnabled(False)
            self.personal_car_model_edit.setEnabled(False)
            self.personal_info_car_color_edit.setEnabled(False)
            self.personal_info_plate_edit.setEnabled(False)
            self.personal_info_car_place_edit.setEnabled(False)
            self.personal_info_member_edit.setEnabled(False)
            self.personal_info_email_edit.setEnabled(False)
        else:

            self.personal_info_phone_edit.setEnabled(True)


    def personal_informatin_submit(self):
        #此列表用来存放个人信息中信息修改的值
        phone_num = self.personal_info_phone_edit.text().strip()
        if self.result[1] != phone_num:
            result = self.car_client.Personal_information_edit(self.result[0], phone_num)
            if result:
                self.personal_info_tooltip_label.setText("恭喜你　修改联系电话成功！！！")
            else:
                self.personal_info_tooltip_label.setText("修改联系电话失败！！！")
        else:
            return




            




class History(Ui_History_stop):
    def __init__(self, car_client):
        super(History, self).__init__()
        self.car_client = car_client
        self.dialog = QDialog()
        self.setupUi(self.dialog)
        


    def show(self, user_name):
        self.user_name = user_name
        self.dialog.show()
        self.click()
        #在历史记录界面打开时，读取数据库历史纪律
        self.get_history()

    def get_history(self):
        self.history_lists = self.car_client.Personal_information_display(self.user_name)

        # 获取用户名
        if self.history_lists[0]:
            self.history_username_info.setText(self.history_lists[0])

            #获取电话号码
            self.history_phonenumber_info.setText(self.history_lists[1])

            #获取汽车厂商
            self.history_car_factory_info.setText(self.history_lists[2])

            #获取车辆型号
            # self.personal_car_model_edit.setText(self.result[5])
            self.history_car_model_info.setText(self.history_lists[3])

            #获取车辆颜色
            # self.personal_info_car_color_edit.setText(self.result[6])
            self.history_car_color_info.setText(self.history_lists[4])

            #获取车牌号
            # self.personal_info_plate_edit.setText(self.result[3])
            self.history_car_plate_info.setText(self.history_lists[5])

            #获取存车记录的停车时间和取车时间
            self.list_historys = self.car_client.Select_history_recording(self.user_name)
           
            # print(self.list_historys)
            
            if self.list_historys[0]:         
                self.history_note_tooltip_label.setText('第1条,共%d条' % (len(self.list_historys)-1))
                if len(self.list_historys)==2:
                    self.history_tooltip_label.setText('没有更多记录了')
                else:
                    self.history_tooltip_label.setText('')
                self.i = 1
                self.history_into_time_info.setText(self.list_historys[self.i][0])
                self.history_leave_tiame_info.setText(self.list_historys[self.i][-1])
        else:
            return



    def click(self):
        # self.i = 0
        self.history_next_note_btn.clicked.connect(self.next_history)
        self.history_previous_note_btn.clicked.connect(self.last_history)  

        
    def next_history(self):
        if self.i == len(self.list_historys):
            self.i = len(self.list_historys)
            return
        else:
            try:
                self.i += 1
                #点击下一页切换页数
                self.history_note_tooltip_label.setText('第%d条,共%d条' % (self.i,len(self.list_historys)-1))
                
                self.history_into_time_info.setText(self.list_historys[self.i][0])
                self.history_leave_tiame_info.setText(self.list_historys[self.i][-1])
            except:
                pass

    def last_history(self):
        if self.i == 1:
            self.i = 1
            self.history_into_time_info.setText(self.list_historys[self.i][0])
            self.history_leave_tiame_info.setText(self.list_historys[self.i][-1])
        else:
            try:
                self.i -= 1
                self.history_note_tooltip_label.setText('第%d条,共%d条' % (self.i,len(self.list_historys)-1))
                self.history_into_time_info.setText(self.list_historys[self.i][0])
                self.history_leave_tiame_info.setText(self.list_historys[self.i][-1])
            except:
                pass




'''
    Modify_username功能直接选用messageAff.py 里的change_user_msg()函数进行处理

    change_user_msg(self,user,phon,email,plat,car,carClass,color)
'''

class Modify_username(Ui_Modify_username_dia):
    def __init__(self,car_client,u_message):
        super(Modify_username, self).__init__()
        self.car_client = car_client
        self.user_message = u_message
        self.dialog = QDialog()
        self.setupUi(self.dialog)
        self.click()

    def show(self, user_name):
        self.user_name = user_name
        self.dialog.show()

    def click(self):
        self.modify_cancle_btn.clicked.connect(self.close)
        self.modify_enter_btn.clicked.connect(self.modify_username)
        

    def close(self):
        self.dialog.close()

    def modify_username(self):
        #获取新的用户名,判断是否能采用,现在只判断格式
        user = self.modify_nsername_edit.text().strip()

        result = self.car_client.Modify_username(self.user_name,user)
        if result[0]:
            self.modify_tooltip_label.setText("<p style='color:red;'>用户名修改成功</p>")
        else:
            html = "<p style='color:red;'>用户名修改失败</p>"
            self.modify_tooltip_label.setText(html)


class Modify_password(Ui_Modify_password_dialog):
    def __init__(self, car_client):
        self.car_client = car_client
        self.dialog = QDialog()
        self.setupUi(self.dialog)
        self.click()

    def show(self, user_name):
        self.user_name = user_name
        self.dialog.show()

    def click(self):
        
        self.modify_password_cancle_btn.clicked.connect(self.close)
        self.modify_password_get_verification_btn.clicked.connect(self.get_email_code_mp)
        self.modify_password_enter_btn.clicked.connect(self.submit_new_password)

    def close(self):
        self.dialog.close()

    def get_email_code_mp(self):
        self.result = self.car_client.Personal_information_display(self.user_name)
        # print(self.result)
        if self.result[0]:
            self.car_client.send_email(self.result[8])
        else:
            return

    def submit_new_password(self):
        new_password = self.modify_nsername_edit.text()
        new_password_again = self.modify_nsername_edit_2.text()
        if new_password == new_password_again:
            result = self.car_client.Modify_password(self.user_name, new_password)
            if result:
                self.modify_password_tooltip_label.setText("密码修改成功")
            else:
                self.modify_password_tooltip_label.setText("密码修改失败")
        else:
            self.modify_password_tooltip_label.setText("密码前后输入不一致,请重新输入")





class Xiala(Ui_Dialog):
    def __init__(self):
        self.dialog = QDialog()
        self.setupUi(self.dialog)
        self.dialog.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    u_message = user_message()

    car_client = carClient()
    # 创建个人资料窗口
    personal = Personal(car_client)
    # 创建历史纪录窗口
    history = History(car_client)
    # 创建修改用户名窗口
    modify_uname = Modify_username(car_client, u_message)
    # 创建修改密码窗口
    modify_password = Modify_password(car_client)

    # 创建主界面
    main = Main(personal, history, modify_uname, modify_password,car_client)

    regist = Regist(car_client)
    forget_password = Forget_Password(car_client)
    login = Login(main, regist, forget_password, car_client)

    sys.exit(app.exec_())













































