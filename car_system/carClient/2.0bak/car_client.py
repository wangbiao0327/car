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

    def init_user(self,mec_list,is_regist=True):
        if is_regist:
            use = mec_list
        else:
            data = 'select_user  %s' % mec_list#向数据库请求用户信息
            self.sockfd.send(data.encode())
            # 向数据库获取信息
            use = self.sockfd.recv(2048).decode().split("  ")
            if use[0] == 'error':
                print("信息初始化错误")
                return 
        self.userName = use[0]
        self.userPhon = use[1]
        self.userEmail = use[2]
        self.userPlat = use[3]
        self.carName = use[4]
        self.carClass = use[5]
        self.carColor = use[6]
        #是否ｖｉｐ有歧义，需根据数据库查询结果判断
        if is_regist:
            self.isVIP = "False"
        else:
            self.isVIP = use[7]
        

    def user(self,account):
        '''
        此函数用来获取用户信息

        此函数能查看用户信息，并且做信息修改
        '''
        print('用户名\t\t:',self.userName)
        print('联系方式\t:',self.userPhon)
        print('邮箱\t\t:',self.userEmail)
        print('车名\t\t:',self.carName)
        print('类型\t\t:',self.carClass)
        print('颜色\t\t:',self.carColor)
        print('车牌号\t\t:',self.userPlat)
        if self.isVIP != "False":
            print('是否VIP\t\t:','是')
        else:
            print('是否VIP\t\t:',"否")
        # 这个choise模拟编辑按钮和退出按钮
        choise = input("编辑(输入(write))or 退出(输入(quit))")
        if choise == 'write':
            user_list = self.mes.change_user_msg(\
                self.userName,self.userPhon,self.userEmail,\
                self.userPlat,self.carName,self.carClass,self.carColor)
            # 这个choise模拟保存按钮和退出按钮
            choise = input('保存(输入(save))or退出(输入(quit))')
            if user_list[0] and choise == 'save':
                data_list = ["change",account]
                data_list = data_list + user_list[1:]
                data = '  '.join(data_list)
                self.sockfd.send(data.encode())
                data = self.sockfd.recv(1024).decode()
                if data == 'ok':
                    print("信息修改成功")
                else:
                    print('信息修改失败')
            elif user_list[0]:
                print("信息错误")

    def select_history(self,account):
        '''
        此函数用来处理历史记录的查询

        参数：账号
        '''
        data = "select_history  %s  %s" % (account,self.userPlat)
        self.sockfd.send(data.encode())
        history = self.sockfd.recv(4096).decode()
        if history == 'no_more':
            print('你没有相关的历史记录了')
        else:
            data_list = history.split('  ')
            for i in data_list:
                mes_list = i.split('##')
                print('========I停车==========')
                print("尊敬的%s：" % self.userName)
                print("你的爱车%s于 %s 使用I停车"%(self.carName,mes_list[0]))
                print("于 %s 离开" % mes_list[1])
                print('=======================')
                print()
                print()
            choise = input("查看更多(输入：more)")
            # 这个choise模拟查看更多历史记录a
            if choise == 'more':
                # self.sockfd.send(b'more')
                self.select_history(account)
            else:
                self.sockfd.send(b'quit')

    def add(self):
        '''
        后期考虑实现
        '''
        pass

    def choise_car(self):
        '''
        后期考虑实现
        '''
        pass

    def change_password(self,account,email,is_forget=False):
        '''
        此类函数用来修改用户密码

        邮箱短信验证码，需要通过邮箱获取短信验证码
        '''
        if is_forget:
            data = 'select_email  %s'% account
            self.sockfd.send(data.encode())
            aff = self.sockfd.recv(1024).decode()
            if aff == 'error':
                # print("未找到你的有邮箱，请确认账号是否有误")
                return "未找到你的有邮箱，请确认账号是否有误"
            else:
                client_email = aff #此处模拟向服务器接受邮箱
                print(aff)
        else:
            client_email = self.userEmail

        if aff == email:

            auth_code = self.mes.my_email(client_email)#返回值为验证码或者false
            return auth_code
        else:
            return "您输入的邮箱和注册邮箱不一致，请检查后再输入"

        # if auth_code:
        #     input_auth_code = input("请输入邮箱验证码")
        #     if input_auth_code == auth_code:
        #         new_password = input("请输入新的密码")
        #         aff_new = input("请再次输入密码")
        #         if new_password != aff_new:
        #             print('前后密码不一致')
        #         # 判断密码是否符合要求
        #         if not self.mes.user_passwd_con(new_password):
        #             print("密码必须为６－１０数字和字母")
        #         #这个choise模拟确认密码和取消按钮
        #         choise = input("确认修改(输入(aff))or取消(输入(quit))")
        #         if choise == 'aff' and new_password == aff_new and \
        #         self.mes.user_passwd_con(new_password):
        #             new_password = self.mes.encrypt(new_password)
        #             data = "change_password  %s  %s" % (account,new_password)
        #             self.sockfd.send(data.encode())
        #             aff = self.sockfd.recv(1024).decode()
        #             if aff:
        #                 print("修改成功")
        #                 return new_password
        #             else:
        #                 self.change_password(self,account,is_forget=False)
        # else:
        #     print("没有收到验证码？点击再次获取")
        #     return "没有收到验证码？点击再次获取"
            # 这个choise模拟确认再次获取验证码
            # choise = input("点击(输入(intp))")
            # if choise == "intp":
            #     self.change_password(account)
            #     return False
        
    def interface(self,account,pid):
        """
        此类函数用来处理客户端登陆后的操作

        功能包括：查看个人信息、查看停车记录、修改用户名、修改密码、接受服务端信息
        """
        while True:
            print("=====请选择相应的功能=====")
            print(1,"个人信息")
            print(2,'停车记录')
            # print(3,'修改用户名') #个人信息已经处理
            print(4,'修改密码')
            print(5,'退出')
            print('=========================')
            choise = input('请选择相应功能')
            if choise == '1':
                self.init_user(mec_list=account,is_regist=False)
                self.user(account)
            elif choise == '2':
                self.select_history(account)
            elif choise == '3':
                pass
            elif choise == '4':
                self.change_password(account)
            elif choise == '5':
                # self.sockfd.send(b"quit")
                os.kill(pid,signal.SIGQUIT)
                break
            else:
                print("请正确输入命令")

    def get_history_msg(self,account,plat):
        '''
        初始化历史信息

        用来接受用户不在线时，服务器发送的信息
        '''
        self.sockfd.close()
        self.sockfd = socket(AF_INET,SOCK_STREAM)
        self.sockfd.connect(ADDR)
        #先给服务器发送一个标志，表示该套接字接受该客户端的信息
        def data_recv(account,plat):
            data = "get_history_msg  %s  %s" % (account,plat)
            self.sockfd.send(data.encode())
            data = self.sockfd.recv(4096).decode()
            if data != 'no_data':
                data_list = data.split("#=#")
                for i in data_list:
                    msg_list = i.split("##")
                    play_msg = msg_list[2].split("  ")
                    if msg_list[1] == "park":
                        print("+++++++++++++I停车++++++++++")
                        print('尊敬的：%s' % self.userName)
                        print("你的车：%s" % self.carName)
                        print("于%s使用I停车"% play_msg[-1])
                        print("位置为：%s" % play_msg[0])
                        print("取车码：%s" % play_msg[1])
                        print("++++++++++++++++++++++++++++")
                        print()
                        print()
                    elif msg_list[1] == 'get_car':
                        print("************I停车***************")
                        print('尊敬的：%s' % self.userName)
                        print("你的车：%s" % self.carName)
                        print("于%s离开车库"% play_msg[-1])
                        print("停车时长：" + play_msg[0])
                        print("费用：" + play_msg[1])
                        print("余额：" + play_msg[2])
                        print("*******************************")
                        print()
                        print()
        data_recv(account,plat)
        while True:
            # 睡十五分钟
            time.sleep(15*60)
            data_recv(account,plat)   

    def msg_handing(self,account,plat):
        '''
        此类函数用来专门处理信息的接收

        参数：账号、车牌
        每隔一段时间就发送一次消息请求
        判断消息类型，做格式化处理，需要创建新的进程和新的套接字
        '''
        p = Process(target=self.get_history_msg,args=(account,plat))
        p.daemon = True
        p.start()
        self.interface(account,p.pid)

    def login(self,account='',password='',is_regist=False,mes_list=[]):
        '''
        此类函数用处理用户登录

        获取用户账号和密码，并发送给服务器
        '''
        account = account
        password = password
        if not account:
            # account = input("请输入账号")
            return "请输入账号"
            #判断手机号是否合法
            if not self.mes.user_phon_con(account):
                # print('手机号错误')
                return 手机号错误
        if not password:
            # password = input("请输入")
            return "请输入密码"
        password = self.mes.encrypt(password)
        # 这个choise模拟登录的点击按钮
        # choise = input('登录(输入login)')
        # if choise == 'login' and self.mes.user_phon_con(account):
        message = 'login  %s  %s' % (account,password)
        self.sockfd.send(message.encode())
        data = self.sockfd.recv(1024).decode()
        if data == 'ok':
            print("登录成功")
            return "登录成功"
            #这里补充用户初始化信息
            # if is_regist:
            #     mes_list = [mes_list[0],mes_list[1],mes_list[2],mes_list[4],mes_list[5],mes_list[6],mes_list[7]]
            #     self.init_user(mes_list,is_regist=is_regist)
            # else:
            #     self.init_user(account,is_regist=is_regist)
            # self.msg_handing(account,self.userPlat)
        else:
            print("登录失败,请正确输入用户信息")
            return  "登录失败,请正确输入用户名或密码"
            # 这个ｃｈｏｉｓｅ模拟登录失败的弹框提示确认按钮
            # choise = input("确认(输入aff)")
            # if choise == 'aff':
            #     return

    def forget(self, account, email):
        '''
        此模块做忘记密码处理

        功能暂时不实现
        '''
        # 由于初始界面就是登录界面，那么用户应该是在登录不上的情况下才会找回密码
        # 所以账号应该是登录界面已经输入的状态下获取，现在下面代码中再次让用户输
        # 入账号！模拟登录不上时获取登录界面的账号值，后期图形界面应该是传入账号
        # account = input("请输入登录账号")

        # account = account
        # 界面同修改密码
        aff = self.change_password(account, email, is_forget=True)
        if aff:
            # self.login(account=account,password=aff,is_regist=False)
            return aff
        else:
            return "修改失败"
            # print("修改失败")

    def regist(self, L):
        '''
        此类方法用来处理用户注册功能

        初步判断用户信息是否合法，并将信息发送给服务器进行处理
        '''
        mes_list = self.mes.gain_message(L)
        if mes_list[0]:
            mes_list[4] = self.mes.encrypt(mes_list[4])
            data_list = ["regist"]
            data_list = data_list + mes_list[1:]
            data = '  '.join(data_list)
            #这个choise模拟点击注册按钮
            # choise = input("注册(输入：regist)")
            # if choise == "regist":
            self.sockfd.send(data.encode())
            aff = self.sockfd.recv(1024).decode()
            if aff == 'ok':
                print('注册成功')
                return '注册成功'
                # self.login(data_list[2],data_list[4],is_regist=True,mes_list=data_list[1:])
            else:
                print(aff)
                return aff
    def send_email(self, my_email):
        self.mes.my_email(my_email)
        

    def main(self):
        while True:
            print("=====请选择相应的功能=====")
            print("1  登录")
            print("2  忘记密码")
            print("3  注册")
            print("4  退出")
            print('=========================')
            choise = '1'
            choise = input("请输入选项")
            # 这个是用来选择登录或注册的，默认是登录界面，目前还没有界面
            # 无法实现，现默认为１，也就是登录界面，分别将忘记密码、注册按钮赋予不同的chois便可跳转
            if choise == '1':
                self.login()
            elif choise == '2':
                self.forget()
            elif choise == '3':
                self.regist()
            elif choise == '4':
                self.sockfd.send(b"quit")
                sys.exit("程序退出")
            else:
                # 图形界面加载后，ｅｌｓｅ字句删除
                print("命令行不准确")

# if __name__ == "__main__":
#     client = carClient()
#     client.main()

