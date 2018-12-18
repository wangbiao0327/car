#A.py
#! /user/bin/env python3
# _*_ coding:utf-8 _*_
    # __author__='谢华明'
import pymysql,time
# import contextlib

class carBarn(object):
    def __init__(self,host="localhost",port=3306,passwd='123456',\
        user="root",db="carBarn",charset='utf8'):
        self.host=host
        self.port=port
        self.user=user
        self.passwd=passwd
        self.db=db
        self.charset=charset
        self.open()
        
    def open(self):
        self.conn=pymysql.connect(host=self.host,port=self.port,\
            user=self.user,passwd=self.passwd,db=self.db,\
            charset=self.charset)
        self.cursor=self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()


#停取车的混合数据库操作

    def judVIP(self,plat):
        '''判断是否为ＶＩＰ，参数：车牌号,返回True或False'''
        sql = 'select userName,phone,VIP,carName,carClass,carColor from client where carPlat = %s;'
        self.cursor.execute(sql,[plat])
        t_mes = self.cursor.fetchone()
        if t_mes:
            return t_mes
        else:
            return "False"

    def judge(self,plat):
        '''判断是否有车位,参数：车牌号,返回车位号或False'''
        if self.judVIP(plat)[2] == "True":
            sql = '''select 专属车位 from cilent where carPlat = %s;'''
            self.cursor.execute(sql,[plat])
            return self.cursor.fetchone()
        else:
            sql = '''select 车位号 from carBarn where 车位状态 = "False";'''
            self.cursor.execute(sql)
            a = self.cursor.fetchone()
            if a:
                return a
            else:
                return False
    def update(self,l):
        '''
        入库函数

        当汽车进入车库时，此函数讲在对应的车位号处插入一条记录
        参数：[车牌号、用户名、联系方式、是否为ＶＩＰ、车名、汽车类型、汽车颜色、车位号]
        '''
        sql = '''update carBarn set 车牌号=%s,
        姓名=%s,联系方式=%s,进入时间=now(),
        车位状态='True',VIP=%s,汽车名称=%s,汽车类型=%s,
        汽车颜色=%s where 车位号=%s;'''
        try:   
            self.cursor.execute(sql,l)
            self.conn.commit()
            return 'ok'
        except Exception as e:
            print('存车失败',e)
            self.conn.rollback()
            return 'error'

    def leave(self,plat):
        '''
        汽车离开记录处理

        当汽车离开车库时，此函数能够向历史记录表插入历史记录，
        并将时时表中该车的记录删除，将车位状态修改
        参数：车牌号
        '''
        sql = '''insert into history select null,carBarn.姓名,
        carBarn.联系方式,carBarn.汽车名称,carBarn.汽车类型,carBarn.汽车颜色,
        carBarn.车牌号,carBarn.进入时间,now()
         from carBarn where carBarn.车牌号=%s;'''
        sqldrop_normal = '''update carBarn set 车牌号=null,姓名=null,
        联系方式=null,进入时间=now(),车位状态="False",VIP='False',
        汽车名称=null,汽车类型=null,汽车颜色=null where carBarn.车牌号=%s;'''
        sqldrop_VIP = '''update carBarn set 车牌号=null,姓名=null,
        联系方式=null,进入时间=now(),车位状态="True",VIP='False',
        汽车名称=null,汽车类型=null,汽车颜色=null where carBarn.车牌号=%s;'''
        try:
            if self.judVIP(plat)[2] == "False" or self.judVIP(plat) == "False":
                self.cursor.execute(sql,[plat])
                self.cursor.execute(sqldrop_normal,[plat])
                self.conn.commit()
            else:
                self.cursor.execute(sql,[plat])
                self.cursor.execute(sqldrop_VIP,[plat])
                self.conn.commit()
        except Exception as e:
            print('插入历史记录失败:',e)
            self.conn.rollback()
            return False

    def select(self,plat):
        '''查询表记录,参数(字符串格式):车牌号'''
        sql = "select * from carBarn where 车牌号 = %s"
        self.cursor.execute(sql,[plat])
        try:
            l = self.cursor.fetchone()
            return True
        except Exception as e:
            return False

#以下是对历史表的操作
    def drop_history(self):
        '''
        删除历史记录

        此函数用来删除历史记录表中，时间大于三个月以前的历史记录
        '''
        sql = '''
            delete from history where leaveTime < (now() - interval 3 month);
        '''
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            #print("删除完成")
        except Exception as e:
            print('删除失败',e)
            self.conn.rollback()
    def hisselect(self,plat):
        '''查询车辆进入时间、出库时间'''
        sqlsele = '''select intoTime,leaveTime
        from history where carPlat = %s order by leaveTime DESC;'''
        self.cursor.execute(sqlsele,[plat])
        data = self.cursor.fetchone()
        if not data:
            return False
        else:
            return data

    def more_history(self,plat):
        sqlsele = '''select intoTime,leaveTime
        from history where carPlat = %s order by leaveTime DESC;'''
        self.cursor.execute(sqlsele,[plat])
        return self.cursor

#以下是注册表的操作
    def insert_login(self,l):
        '''注册表添加信息;传入账号,密码,邮箱列表'''
        sql="insert into login values(%s,%s,%s);"
        try:
            self.cursor.execute(sql,l)
            self.conn.commit()
            return True
        except Exception as e:
            print('login:',e)
            return False
    def delete_login(self,phone):
      '''删除注册表信息;传入账号'''
      sql="delete from login where phone=%s;"
      try:
          self.cursor.execute(sql,[phone])
          self.conn.commit()
      except Exception as e:
          print('删除注册表信息失败')
    def update_login(self,l):
        '''修改注册表;传入账号,密码,邮箱列表'''
        sql="update login set password=%s where phone=%s;"
        try:
            self.cursor.execute(sql,l)
            self.conn.commit()
            return True
        except Exception as e:
            print('修改注册表失败')
            return False

    def update_email(self,l):
        '''修改注册表;传入账号,邮箱列表'''
        sql="update login set email=%s where phone=%s;"
        try:
            self.cursor.execute(sql,l)
            self.conn.commit()
            return True
        except Exception as e:
            print('修改注册表失败')
            return False

    def get_password(self,phone):
        '''获取账号对应的用户信息;返回密码'''
        try:
            sql="select password,email from login where phone=%s"
            self.cursor.execute(sql,[phone])
            a=self.cursor.fetchone()
            if a:
                return a
            else:
                return False
        except Exception as e:
            print('查询注册表失败,可能是mysql模块语法错误',e)
            return False


#以下是client表的操作
    def insert_client(self,l):
        '''插入数据;传入用户信息列表:[userName phone carName carClass carColor
                       carPlat 专属车位 VIP 第二账户]'''
        try:
            sql="insert into client values(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            self.cursor.execute(sql,l)
            self.conn.commit()
            return True
        except Exception as e:
            print('client',e)
            return False
    def delete_client(self,phone):
        '''删除数据;传入账号'''
        try:
            sql="delete from client where phone=%s"
            self.cursor.execute(sql,[phone])
            self.conn.commit()
        except Exception as e:
            print('删除用户信息表失败')
    def update_client(self,l,account=''):
        '''修改数据;传入用户列表:[userName phone carName carClass carColor
                       carPlat 专属车位 VIP 第二账户]'''
        try:
            sql="update client set userName=%s,phone=%s,carName=%s,\
                carClass=%s,carColor=%s,carPlat=%s,专属车位=%s,VIP=%s,phone2=%s where phone2=%s;"
            self.cursor.execute(sql,l+[account])
            self.conn.commit()
            return True
        except Exception as e:
            print('插入用户信息表失败:',e)
            return False
    def select_client(self,phone):
        '''查看数据;传入账号,返回列表'''
        try:
            sql="select * from client where phone2=%s"
            self.cursor.execute(sql,[phone])
            return self.cursor.fetchone()
        except Exception as e:
            print('查询注册表失败,可能是mysql模块语法错误:',e)
            return False

    def select_plat(self,car_plat):
        '''
        查看车牌是否已经被注册

        参数：车牌号：
        返回：True or False
        '''
        sql = '''select carPlat from client where carPlat = %s'''
        self.cursor.execute(sql,[car_plat])
        try:
            if self.cursor.fetchall():
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

#以下是对缓存信息表的操作
    def insert_msg(self,l):
        '''插入信息;传入列表:[plat,class,text]'''
        try:
            sql="insert into msg values(%s,%s,%s);"
            self.cursor.execute(sql,l)
            self.conn.commit()
            return True
        except Exception as e:
            print('插入缓存信息表失败:',e)
            return False

    def delete_msg(self,plat):
        '''删除信息;传入车牌号'''
        try:
            sql="delete from msg where plat=%s;"
            self.cursor.execute(sql,[plat])
            self.conn.commit()
            print("已经执行了删除操作")
            return True
        except Exception as e:
            self.conn.rollback()
            print('删除缓存信息表失败',e)
            return False
    def select_msg(self,plat):
        '''查询信息;传入车牌号'''
        try:
            sql="select * from msg where plat=%s;"
            self.cursor.execute(sql,[plat])
            mes_tup = self.cursor.fetchall()
            if mes_tup:
                return mes_tup
            return False
        except Exception as e:
            self.conn.rollback()
            print('查询信息表失败',e)
            return False
