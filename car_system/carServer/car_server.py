"""
此模块做停车管理系统的服务端

Author:Recall
Date: 2018-10-15
module: socket、Thread、sys、os、time
Email:
"""
from socket import *
from threading import Thread
from setting import *
from car_mysql import *
from mysql_function import *
import sys,os,time,random



class car_server(object):
    def __init__(self):
        self.sockfd = socket(AF_INET,SOCK_STREAM)
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(ADDR)
        self.sockfd.listen(5)
        self.client = Client_function()
        self.login = Login_fuction()
        self.carbarn = Carbarn_function()
        self.history = History_function()
        self.weather = Weather_function()
        self.take_car = ["5732",'1103','5959']
        self.date_dict = {"Jan":"一月","Feb":"二月",\
        "Mar":"三月","Apr":"四月","May":"五月","Jun":"六月",\
        "Jul":"七月","Aug":"八月","Sep":"九月","Oct":"十月",\
        "Nov":"十一月","Dec":"十二月"}

    def park(self,c,plate):
        '''
        此函数用来做停车处理

        参数：套接字，车牌号
        此类函数获取车位位置，并将修改数据库表的时时表数据信息
        '''
        result = self.carbarn.stop_car(plate)
        print("停车状况：",result)
        if not result[0]:
            c.send(b'error')
            return
        take_car = ''
        for i in range(6):
            take_car += str(random.randint(0,9))
        self.take_car.append(take_car)
        posit = result[1]
        data = "ok  %s  %s" % (str(posit),take_car)
        c.send(data.encode())


    def cost(self, into_time, leave_time, money=1000):
        '''
        计算停车费用

        参数：进入时间、离开时间、余额
        暂时未考虑账户余额，后期考虑加入，现默认为１０００
        返回：停车时长、费用、余额
        '''
        parttime = leave_time - into_time
        t = parttime.days
        seconds = parttime.seconds
        h = seconds // 3600
        m = (seconds - h *3600) // 60
        
        if t == 0 and h > 0:
            p_time = '%d 小时 %d 分' %(h,m)
        elif t == 0 and t == 0 and m > 20:
            p_time = ' %d 分' %(m)
        elif t ==0 and h == 0 and m < 20:
            p_time = '%d 分钟' % 20
        else:
            p_time = '%d 天 %d 小时 %d 分' %(t,h,m)

        consumption = (t*24)*3+h*5
        print('本次消费',consumption,'元')
        money -= consumption
        if money < consumption:
            print('余额不足,请及时充值')
        return (p_time,consumption,money)
                
    def get_car(self,c,plate,take_car):
        '''
        此函数用作处理取车处理

        参数：套接字、车牌
        功能：通过车牌号判断当前车辆是否停放在车库内，根据判断结果作相应处理
        如果车辆停放在车库内，则计算停车时长和停车费用，并将消息分别发送给管
        理器和存入信息列表
        '''
        if take_car not in self.take_car:
            c.send('验证码错误'.encode())
            return
        try:
            # 更新车库车位信息
            result = self.carbarn.get_car(plate)
            if result[0]:
                self.history.insert_history(plate)
                history = self.history.select_history_by_plat(plate)[1]
                cost = self.cost(history[0],history[1])
                self.carbarn.update_car_is_stop(plate)
                data = "ok  %s" % cost[1]
                c.send(data.encode())
                return
            c.send("取车失败".encode())
        except Exception as e:
            print("取车失败：",e)
            c.send("服务器发生异常错误".encode())

    def Login(self,c,username,password):
        '''
        此函数做登录信息的处理

        判断用户信息是否正确
        '''
        #此处模拟向数据库用户信息表查询用户密码，传入参数为username
        try:
            user_message = self.login.select_user_information(username)
        except Exception as e:
            c.send(b'error')
        if user_message[0]:
            if user_message[1][2] == password and user_message[1][4] == "False":
                self.login.modify_login_status(username,"True")
                c.send(b'ok')
            elif user_message[1][2] != password:
                c.send(b'passerror')
            elif user_message[1][4] != "False":
                c.send(b'online')
        else:
            c.send(b'error')

    def regist(self,c,username, password, phone_number, car_factory, car_model, car_color, car_plate, email):
        '''
        此函数用来做注册时信息处理

        对用户信息做二次判断，如账号或车牌号已经进行注册，
        若信息均无误，将信息进行存储处理
        '''

        # [username, password, phone_number, car_factory, car_model, car_color, car_plate, email]
        # 此处判断用户名是否已经注册
        user_name = self.client.select_user_by_username(username)
        # 判断车牌号号是否已经被注册
        user_plate = self.client.select_user_by_plate(car_plate)

        if user_name[0] :
            c.send("该用户名早已进行注册".encode())
            return
        elif user_plate[0]:
            c.send("该车牌号早已进行注册".encode())
            return
        #下面是对信息处理的操作,将信息存入到数据库
        try:
            self.client.add_genral_user(username, phone_number, car_factory, car_model, car_color, car_plate)
            id = self.client.select_user_by_username(username)[1][0]
            self.login.add_user(id,username,password,email)
            c.send("ok".encode())
        except Exception as e:
            if self.login.select_user_information(username)[0]:
                self.login.delete_user()
            self.login.conn.rollback()
            c.send("注册失败，请重新注册".encode())
            return

    def select_user(self,c,username):
        '''
        此函数用来查询用户信息

        参数：用户名
        向数据库查询用户信息
        '''
        try:
            user_login_list = self.login.select_user_information(username)
            user_client_list = self.client.select_user_by_username(username)
            if user_client_list[0] and user_login_list[0]:
                # username,phone_number,car_factory,car_model,car_color,car_plate,car_place,member,email
                user_list = ['ok'] + list(user_client_list[1][2:8]) + [str(user_client_list[1][8])] + [user_client_list[1][-1]] +[user_login_list[1][3]]
                data = '  '.join(user_list)
                c.send(data.encode())
                return
            c.send("not fount  sorry".encode())
        except Exception as e:
            print("查询用户信息失败：",e)
            c.send("not fount  sorry".encode())

    def get_weath_message(self,c,city):
        '''
        此函数用来查询天气信息，并返回给客户端
        '''
        try:
            result = self.weather.select_weather(city)
            if result[0]:
                now_hour = time.localtime().tm_hour
                if 6 <= now_hour <= 18:
                    data = '  '.join(result[1][1:5])
                else:
                    data = "  ".join(result[1][-4:])
                c.send(data.encode())
            else:
                c.send(b"error")
        except Exception as e:
            c.send(b"error")
            print("查询天气失败：",e)


    def change_password(self,c,username,password):
        '''
        此函数用来处理用户密码的修改

        参数：用户名　密码
        '''
        try:
            self.login.modify_password(username,password)
            c.send(b'ok')
        except:
            c.send(b"error")

    def change_username(self,c,oldname,newname):
        '''
        此函数用来处理用户名修改

        参数：旧用户名　新用户名
        将用户名传到数据库，并进行判断，如果已经在数据库，则不修改
        '''
        try:
            user = self.login.select_user_information(newname)
            print(user)
            id = self.login.select_user_information(oldname)[1][0]
            if user[0]:
                c.send("nameisuser".encode())
                return
            self.login.modify_username(id,newname)
            c.send(b"ok")
        except Exception as e:
            print("修改用户名错误：",e)
            c.send(b'error')

    def change_user_message(self,c,username,phone_number):
        '''
        修改用户联系方式

        将用户联系方式进行修改
        '''
        try:
            aff = self.client.modify_user_phone(username,phone_number)
            if aff:
                c.send(b'ok')
                return
            c.send(b'error')
        except:
            c.send(b'error')

    def select_email(self,c,username,email):
        '''
        获取用户邮箱

        参数：套接子、帐号
        '''
        # 向数据库获取邮箱
        try:
            client_email = self.login.select_user_information(username)[1][3]
            if client_email == email:
                c.send(b'ok')
            else:
                c.send(b"error")
        except Exception as e:
            print("获取用户邮箱错误：",e)
            c.send(b'error')
            return

    def get_history_msg(self,c,username,aff):
        '''
        获取用户历史记录

        向数据库查询用户历史记录并发送给客户端
        '''
        try:
            plate = self.client.select_user_by_username(username)[1][-3]
            history_lister = self.history.select_history_by_plat(plate,int(aff)*5)
            if history_lister[0]:
                data = ''
                for i in history_lister[1:]:
                    data += str(i[0]) + "##" + str(i[1]) + "  "
                c.send(data.encode())
                return
            c.send(b"error")
        except Exception as e:
            print("查询历史记录失败：",e)
            c.send(b"error")

    def User_quit(self,c,username):
        try:
            aff = self.login.modify_login_status(username,"False")
            if aff[0]:
                c.send(b"ok")
                return
            c.send(b"error")
        except Exception as e:
            c.send(b"error")
            print("修改用户登录状态失败：",e)

    def child_thread(self,c):
        '''
        此函数用来处理客户端的链接请求

        包括登录、注册、信息修改、车辆信息查询等
        '''
        while True:
            data = c.recv(4096).decode()
            if not data:
                break
            data = data.split('  ')
            if data[0] == 'login':
                self.Login(c,data[1],data[2])
            elif data[0] == 'regist':
                self.regist(c,data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8])
            elif data[0] == 'change_password':
                self.change_password(c,data[1],data[2])
            elif data[0] == "change_username":
                self.change_username(c,data[1],data[2])
            elif data[0] == 'change_user_message':
                self.change_user_message(c,data[1],data[2])
            elif data[0] == "select_user_message":
                self.select_user(c,data[1])
            elif data[0] == 'get_history_msg':
                self.get_history_msg(c,data[1],data[2])
            elif data[0] == "select_weath_message":
                self.get_weath_message(c,data[1])
            elif data[0] == "select_email":
                self.select_email(c,data[1],data[2])
            elif data[0] == 'quit':
                self.User_quit(c,data[1])
                c.close()
                break

    def drop_history(self):
        # 此函数用来定期删除历史记录
        while True:
            self.history.delete_history()
            time.sleep(30*24*60*60)

    def Update_weather(self):
        #此函数定时更新车库天气信息表信息
        hour = time.localtime().tm_hour
        min = time.localtime().tm_min
        if 0 <= hour < 6:
            time_sleep = 6 * 60 * 60 - hour * 60 *60 - min * 60
        elif 6 < hour < 18 or (hour == 6 and min>0):
            time_sleep = 18 * 60 * 60 - hour * 60 *60 - min * 60
        elif hour > 18 or (hour==18 and min >0):
            time_sleep = (24+6) * 60 * 60 - hour * 60 * 60 - min * 60
        else:
            time_sleep = 0
        print(time_sleep)
        try:
            if time_sleep:
                self.weather.delete_weather()
                self.weather.add_data()
                time.sleep(time_sleep)
            while True:
                try:
                    self.weather.delete_weather()
                    self.weather.add_data()
                    time.sleep(12*60*60)
                except Exception as e:
                    print("天气更新失败：", e)
        except Exception as e:
            print("天气更新失败：",e)

    def adminis(self):
        '''
        服务器与车库管理交互函数

        用来循环接受车库管理具体请求
        给出判断并作出相应处理
        '''
        self.sockfd = socket(AF_UNIX,SOCK_STREAM)
        if os.path.exists("sock_file"):
            os.unlink("sock_file")
        self.sockfd.bind("sock_file")
        self.sockfd.listen(5)
        try:
            c,addr = self.sockfd.accept()
            print("管理接口",addr)
        except Exception as e:
            print("服务器发生未知错误：",e)
        while True:
            data = c.recv(1024).decode()
            print(data)
            choise_list = data.split('  ')
            if choise_list[0] == 'park':
                self.park(c,choise_list[1])
            elif choise_list[0] == 'get_car':
                self.get_car(c,choise_list[1],choise_list[2])
            else:
                print('出现未知命令')
                break

    def main(self):
        pid = os.fork()
        if pid < 0:
            self.sockfd.close()
            sys.exit('创建进程失败')
        elif pid == 0:
            self.adminis()
        else:
            dro = Thread(target = self.drop_history)
            update_weather = Thread(target=self.Update_weather)
            dro.start()
            update_weather.start()
            while True:
                try:
                    c,addr = self.sockfd.accept()
                    print('欢迎',addr)
                except KeyboardInterrupt:
                    self.sockfd.close()
                    sys.exit(0)
                except Exception as e:
                    print(e)
                    continue
                t = Thread(target=self.child_thread,\
                    args=(c,))
                t.setDaemon(True)
                t.start()

if __name__ == '__main__':
    car_db = car_server()
    car_db.main()