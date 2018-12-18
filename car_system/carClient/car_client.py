"""
此模块做停车管理系统的客户端

Author:Recall
Date: 2018-10-1９
module: socket、multiprocessing、sys、os、time、signal
Email:
"""

from socket import *
from setting import *
from messageAff import user_message
from multiprocessing import Process
import sys,os,time,signal


class carClient(object):
    def __init__(self):
        self.sockfd = socket(AF_INET,SOCK_STREAM)
        self.sockfd.connect(ADDR)
        self.mes = user_message()
        signal.signal(signal.SIGINT,self.dis_signal)

    def dis_signal(self,sig,frame):
        if sig == signal.SIGINT:
            self.sockfd.send(b'quit')
            sys.exit("强制退出")
        elif sig == signal.SIGQUIT:
            self.sockfd.send(b'quit')

    def Get_email_verify_code(self,username,email):
        '''
        获取验证码

        将用户名跟邮箱发送到服务器进行数值判断，并根据判断进行返回
        返回值：verify_code or False
        '''
        data = 'select_email  %s  %s'% (username,email)
        self.sockfd.send(data.encode())
        aff = self.sockfd.recv(1024).decode()
        if aff == 'ok':
            auth_code = self.mes.my_email(email)
            return auth_code
        else:
            return [False,"你输入的邮箱与注册的邮箱不一致"]

    def Modify_password(self, username, password):
        '''
        此函数用来处理密码的修改

        参数：用户名　密码
        将用户密码发送到服务器，根据服务器信息确认处理
        返回值：True or False
        '''
        data = "change_password  %s  %s" % (username,password)
        self.sockfd.send(data.encode())
        aff = self.sockfd.recv(1024).decode()
        if aff == "ok":
            return True
        return False

    def Modify_username(self,olduesrname,newusername):
        '''
        此函数用来修改用户名称

        参数：旧用户名　　新用户名
        将新旧用户名发送到服务器，并根据服务器返回值进行返回
         返回值：
            成功：True
            失败：
                [False,"用户名早已被使用"]
                [False,'修改用户名失败']
        '''
        data = 'change_username  %s  %s' % (olduesrname,newusername)
        self.sockfd.send(data.encode())
        aff = self.sockfd.recv(1024).decode()
        if aff == "ok":
            return [True]
        elif aff == "nameisuser":
            return [False,"用户名早已被使用"]
        return [False,'修改用户名失败']

    def Personal_information_display(self,username):
        '''
        此函数用来获取用户信息

        参数：用户名
        向服务器发送用户名，通过服务器返回值进行返回
        '''
        data = "select_user_message  %s" % username
        try:
            self.sockfd.send(data.encode())
        except:
            return [False]
        aff = self.sockfd.recv(1024).decode()
        user_list = aff.split("  ")
        if user_list[0] == "ok":
            return user_list[1:]
        return [False,"未找到用户信息"]

    def Personal_information_edit(self,username,phone_number):
        '''
        此函数用来修改用户信息

        参数：用户名　联系方式
        发送到服务器修改用户的联系方式
        返回值：True or False
        '''
        data = "change_user_message  %s  %s" % (username,phone_number)
        self.sockfd.send(data.encode())
        aff = self.sockfd.recv(1024).decode()
        if aff == "ok":
            return True
        return False

    def Select_history_recording(self,username,aff=0):
        '''
        向服务器获取用户历史记录

        参数：用户名　偏识标量
        aff:偏识标量,假设用户有十五条历史记录，传入aff=2则返回结果为用户第１１条至第１５条的历史记录
        返回历史记录，每次返回５条，不足五条或五条返回全部历史记录
        返回值：
            有历史记录：[True,[],[]....],每个小列表为一条记录
            无历史记录：[False]
        '''
        data = "get_history_msg  %s  %d" % (username,aff)
        self.sockfd.send(data.encode())
        aff = self.sockfd.recv(4096).decode()
        history_list =[True]
        if aff != "error":
            history_str = aff.split("  ")
            for i in history_str:
                record = i.split("##")
                history_list.append(record)
            return history_list
        return [False]

    def Login(self,username,password):
        '''
        此类函数用处理用户登录

        参数：用户名　密码
        返回值:
            成功:True
            失败：
                [False,"用户名或密码错误"]
                [False,"你已经在线，不能重复登录"]
        获取用户账号和密码，并发送给服务器
        '''
        message = 'login  %s  %s' % (username, password)
        self.sockfd.send(message.encode())
        aff = self.sockfd.recv(1024).decode()
        if aff == "ok":
            return [True]
        elif aff == "passerror":
            return [False,"用户名或密码错误"]
        elif aff == "online":
            return [False,"你已经在线，不能重复登录"]
        return [False, "用户名或密码错误"]

    def Register(self, username,password,phone_number,car_factory,car_model,car_color,car_plate,email):
        '''
        此类方法用来处理用户注册功能

        初步判断用户信息是否合法，并将信息发送给服务器进行处理
        返回值：
            成功：True
            失败:
                [False,"该用户名早已进行注册"]
                [False,"该车牌号早已进行注册"]
        '''
        print("进入了car_lient的注册函数")
        L = [username,password,phone_number,car_factory,car_model,car_color,car_plate,email]
        data_list = ["regist"] + L
        data = "  ".join(data_list)
        self.sockfd.send(data.encode())
        aff = self.sockfd.recv(1024).decode()
        if aff == 'ok':
            return [True]
        return [False,aff]

    def User_quit(self,username):
        '''
        此函数在用户退出时修改用户的登录状态

        参数：用户名
        返回值：True or False
        '''
        data = 'quit  %s' % username
        self.sockfd.send(data.encode())
        aff = self.sockfd.recv(1024).decode()
        if aff == "ok":
            return  True
        return False

    def Select_weath_message(self,city):
        """
        此函数用来获取天气信息

        参数：城市名
        返回值为列表：
            成功：[True,{}],如：[True, {'wind_power': '<3级', 'min_temper': '17', 'wind_direction': '无持续风向', 'weather': '多云'}]
            注意字典气温参数，夜间为最低气温min_temper，白天为最高气温ｍａｘ_temper
            失败：[False]
        """
        data = "select_weath_message  %s" % city
        self.sockfd.send(data.encode())
        aff = self.sockfd.recv(1024).decode()
        if aff != "error":
            weath_list = aff.split("  ")
            now_hour = time.localtime().tm_hour
            if 6 <= now_hour <= 18:
                dic = {
                    "weather":weath_list[0],
                    "wind_direction":weath_list[1],
                    "wind_power":weath_list[2],
                    "max_temper":weath_list[3]
                }
            else:
                dic = {
                    "weather": weath_list[0],
                    "wind_direction": weath_list[1],
                    "wind_power": weath_list[2],
                    "min_temper": weath_list[3]
                }
            return [True,dic]
        return [False]

    def send_email(self, my_email):
        self.mes.my_email(my_email)
        

if __name__ == "__main__":
    client = carClient()
    # [username, password, phone_number, car_factory, car_model, car_color, car_plate, email]
    # print(client.Register("杨军军","123456","15767517285","奥迪","A8","黑色","粤B.66666","2089850364@qq.com"))
    # print(client.Login("杨军军","654321"))
    # print(client.Get_email_verify_code("杨军军","2089850364@qq.com"))
    # print(client.Modify_password("杨军军","654321"))
    # print(client.Modify_username("楊軍軍","楊軍軍"))
    while True:
        name = input("输入username")
        print(client.Personal_information_display(name))
    # print(client.Select_history_recording("楊軍軍"))
    # print(client.Personal_information_edit("楊軍軍",'13788888888'))
    # print(client.Select_weath_message("深圳市"))
    # print(client.User_quit("楊軍軍"))