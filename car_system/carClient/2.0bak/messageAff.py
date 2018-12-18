'''
此模块主要用来判断用户信息获取模板类

Author:Recall
Date:2018-09-19
module:re、random、smtplib
'''
import re,random,smtplib,hashlib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

class user_message(object):
    # def __init__(self, arg):
    #     super(user_message, self).__init__()
    #     self.arg = arg

    def user_name_con(self,name):
        '''此类方法用来判断用户名是否正确'''
        nameList = re.findall(r"\d+|\W+|^\s+$ ",name)
        if nameList:
            return False
        else:
            nameList2 = re.findall(r"^[\u4E00-\u9FA5]+$",name)
            if nameList2:
                return True
            else:
                return False

    def user_phon_con(self,phon):
        '''此类方法用来判断用户号码是否合法'''
        phoneList = re.findall(r'^1[3,4,5,7,8][0-9]{9}$',phon)
        if phoneList:
            return True
        else:
            return False

    def user_email_con(self,email):
        patt = r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$'
        email_list = re.search(patt,email)
        if email_list:
            if re.search(patt,email).group():
                return True
            return False
        else:
            return False

    def user_passwd_con(self,passwd):
        '''此类方法用来判断密码是否合法，密码必须为6-10数字跟字母结合'''
        pattList = [r'^[0-9]{6,10}$',r'^[a-zA-Z]{6,10}$']
        for i in pattList:
            if re.findall(i,passwd):
                return False
        passwdList = re.findall(r'^[0-9a-zA-z]{6,10}$',passwd)
        if passwdList:
            return True
        else:
            return False

    def user_plate_con(self,plate):
        '''此方法判断用户车牌号是否合法'''
        l=['京','津','沪','渝','宁','藏','新','蒙','澳','黑','吉','皖','鲁',\
        '晋','粤','桂','苏','赣','冀','豫','浙','琼','鄂','湘','甘','闽','川','贵','辽','陕','青','台']
        patt=r'^'+'{}'.format(l) + r'[A-Z]{1}\.[A-Z0-9]{5}$'
        plate_number_list = re.findall(patt,plate)
        if plate_number_list:
            return True
        else:
            return False

    def gain_message(self, L):
        '''
        此类方法用于获取用户信息，并且做简单的逻辑判断

        返回用户的信息列表,此处打印均为用户将信息输入错误时的文本提示
        '''
        # name = input("请输入用户名")
        # if not self.user_name_con(name):
        #     print("请输入正确的中文名，不能包含英文字母，如：张三")
        # phone = input("请输入有效的手机号,手机号将成为登录的唯一凭证")
        # if not self.user_phon_con(phone):
        #    print("请输入合法的手机号码")
        # email = input("请输入邮箱，邮箱将作为密码丢失时验证")
        # if not self.user_email_con(email):
        #     print("请输入合法的邮箱")
        # password = input("请输入6-10位数字、字母")
        # if not self.user_passwd_con(password):
        #     print("密码不符合要求,必须为6-10字母和数字结合")
        # plate_number = input("请输入车牌号")
        # if not self.user_plate_con(plate_number):
        #     print("请输入合法车牌号")
        # car_name = input("请输入汽车名称")
        # car_class = input("请输入汽车类型")
        # car_color = input("请输入汽车颜色")

        name = L[0]
        if not self.user_name_con(name):
            print("请输入正确的中文名，不能包含英文字母，如：张三")
        password = L[1]
        if not self.user_passwd_con(password):
            print("密码不符合要求,必须为6-10字母和数字结合")

        phone = L[3]
        if not self.user_phon_con(phone):
           print("请输入合法的手机号码")

        car_name= L[4]

        car_class = L[5]

        car_color = L[6]

        plate_number = L[7]
        if not self.user_plate_con(plate_number):
            print("请输入合法车牌号")

        email = L[8]
        if not self.user_email_con(email):
            print("请输入合法的邮箱")

        verification_code = L[9]
        if self.auth_code != verification_code:
            return "验证码不正确"


        if self.user_name_con(name) and self.user_phon_con(phone) and \
        self.user_passwd_con(password) and self.user_plate_con(plate_number):
            return [True, name, phone,email, password,\
             plate_number, car_name, car_class, car_color]
        else:
            print("请输入正确的信息")
            return [False, name, phone,email, password,\
             plate_number, car_name, car_class, car_color]

    def judge_user_number(self):
        '''此类方法用于判断用户车辆数量判断
            
        '''
        pass

    def change_user_msg(self,user,phon,email,plat,car,carClass,color):
        '''此类方法用于修改用户信息

        当用户不输入内容时，信息为原有信息，所有打印均为用户输入错误时的信息提示
        '''
        name = input("请输入用户名")
        if name == '':
            name = user
        elif not self.user_name_con(name):
            print("用户名不合法")
        phone = input("请输入有效的手机号码")
        if phone == '':
            phone = phon
        elif not self.user_phon_con(phone):
            print("电话号码有误，请重新输入")
        uemail = input("请输入合法邮箱")
        if uemail == '':
            uemail = email
        elif not self.user_email_con(uemail):
            print("请输入合法邮箱")
        car_name = input("请输入汽车名")
        if car_name == '':
            car_name = car
        car_class = input("请输入汽车类型")
        if car_class == '':
            car_class = carClass
        car_color = input('请输入汽车颜色')
        if car_color == '':
            car_color = color
        plate_number = input("请输入车牌号")
        if plate_number == '':
            plate_number = plat
        elif not self.user_plate_con(plate_number):
            print("请输入合法车牌号")

        if self.user_name_con(name) and self.user_phon_con(phone) and\
        self.user_email_con(uemail) and self.user_plate_con(plate_number):
            return [True,name,phone,uemail,plate_number,car_name,car_class,car_color]
        else:
            return [False,name,phone,uemail,plate_number,car_name,car_class,car_color]

    def encrypt(self,password):
        s = hashlib.sha1()
        s.update(password.encode('utf-8'))
        return s.hexdigest()

    def my_email(self,my_email):
        import smtplib,time,random
        from email.mime.text import MIMEText
        from email.utils import formataddr
        my_sender = '1097943765@qq.com'    # 发件人邮箱账号
        my_pass = 'zxnamzlysgdrhccj'       # 此处为授权密码，现用'xxxxxxx'代替
        my_user = my_email      # 收件人邮箱账号，我这边发送给自己
        auth_code_head = '这是我的验证码，一般人我都不告诉他：'
        self.auth_code = ''
        auth_code = ''
        for i in range(4):
            auth_code += str(random.randint(0,9))


        self.auth_code = auth_code
        auth_code = auth_code_head + auth_code
        #由于校内电脑无法发送邮箱，下面三行代码为测试阶段使用，正常运行时应删除下面三行代码，
        # 否则影响程序正常运行
        # print("由于校内电脑无法发送邮箱,下面为邮箱内容，本行代码测试时使用，正式使用时\
        #     请删除本行及下面两行代码")
        # print(auth_code)
        # return auth_code[-4:]
        def mail(auth_code):
            ret = True
            try:
                msg = MIMEText(auth_code, 'plain', 'utf-8')
                # 括号里的对应发件人邮箱昵称、发件人邮箱账号
                msg['From'] = formataddr(["I停车", my_sender])
                # 括号里的对应收件人邮箱昵称、收件人邮箱账号
                msg['To'] = formataddr([my_user, my_user])
                msg['Subject'] = "I停车"           # 邮件的主题，也可以说是标题
                print("-----------------")

                # 发件人邮箱中的SMTP服务器，端口是４６５
                server = smtplib.SMTP_SSL("smtp.qq.com", 465)
                print('+++++++++++++')
                server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
                # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
                server.sendmail(my_sender, [my_user, ], msg.as_string())
                server.quit()  # 关闭连接
            except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
                print(e)
                ret = False
            return ret

        ret = mail(auth_code)
        if ret:
            print("邮件发送成功")
            return auth_code[-4:]
        else:
            print("邮件发送失败")
            return False

        
