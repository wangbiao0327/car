'''
此模块用于初始化此项目要用到的数据库CarBarn
运行此模块可以创建数据库CarBarn
以及CarBarn里面的４张表

client
login
history
carbarn
weather


'''
import pymysql


class Client(object):
    """创建CarBarn库，以及client表"""
    def __init__(self,information_schema,database_name,host="localhost",
                 user="root",password="123456",
                 charset="utf8",port=3306):
        self.database = information_schema
        self.database_name = database_name
        self.host = host
        self.user = user 
        self.password = password
        self.charset = charset
        self.port = port
        self.open()

    # 连接数据方法
    def open(self):
        # 创建conn
        self.conn = pymysql.connect(host=self.host,
                user=self.user,password=self.password,
                database=self.database,
                charset=self.charset,
                port=self.port)
        # 创建游标cur
        self.cur = self.conn.cursor()

    # 关闭
    def close(self):
        self.cur.close()
        self.conn.close()

    def create_database(self):     
        #创建数据库
        sql = "create database %s" % self.database_name
        try:
            self.cur.execute(sql)
            self.conn.commit()
            print('创建数据库成功')
        except Exception as e:
            self.conn.rollback()
            print('error:%s' % e)
            return '创建数据库失败'

        sql = 'use %s ' % self.database_name
        try:
            self.cur.execute(sql)
            self.conn.commit()
            print('进入到%s库' % self.database_name)
        except Exception as e:
            self.conn.rollback()
            print('error:%s' % e)
            return '切换%s库失败' % self.database_name

        self.create_table_client()

    def create_table_client(self):
        '''
        创建表client,login,history,carbarn

        '''
        #切换数据库
        sql = 'use %s' % self.database_name
        self.cur.execute(sql)

         #创建carbarn表
        sql = "create table  carbarn(id int(3) auto_increment PRIMARY KEY,\
                                               car_place int(3) zerofill unique default null,\
                                               car_plate varchar(100) ,\
                                               into_time datetime,\
                                               isStop enum('True','False') default 'False',\
                                               member enum('True','False') default 'False')character set utf8;"


        try:
            self.cur.execute(sql)
            self.conn.commit()
            print('创建carbarn表成功')
        except Exception as e:
            self.conn.rollback()
            print('error:%s' % e)
            return '创建carbarn表失败'

        #创建client表
        sql = "create table client(id int auto_increment PRIMARY KEY,\
                                    name varchar(100) not null unique,\
                                    username varchar(100) not null unique,\
                                    phone_number varchar(50),\
                                    car_factory  varchar(150),\
                                    car_model varchar(100),\
                                    car_color varchar(100),\
                                    car_plate varchar(100) unique ,\
                                    car_place int(3) zerofill,\
                                    member enum('True','False') default 'False',\
                                    foreign key(car_place) references carbarn(car_place))character set utf8;"
        try:
            self.cur.execute(sql)
            self.conn.commit()
            print('创建client表成功')
        except Exception as e:
            self.conn.rollback()
            print('error:%s' % e)
            return '创建client表失败'

        #创建login表
        sql = "create table login(id int,\
                                  username varchar(100) not null ,\
                                  password varchar(200) not null,\
                                  email varchar(200) not null ,\
                                  isLogin enum('True','False') default 'False',\
                                  isActive enum('True','False') default 'True',\
                                  foreign key(id) references client(id)\
                                  )character set utf8;"
        try:
            self.cur.execute(sql)
            self.conn.commit()
            print('创建login表成功')
        except Exception as e:
            self.conn.rollback()
            print('error:%s' % e)
            return '创建login表失败'
        

        #创建history表
        sql = "create table history(id int auto_increment PRIMARY KEY,\
                                    car_plate varchar(100) not null,\
                                    into_time datetime,\
                                    leave_time timestamp)character set utf8;"

        try:
            self.cur.execute(sql)
            self.conn.commit()
            print('创建history表成功')
        except Exception as e:
            self.conn.rollback()
            print('error:%s' % e)
            return '创建history表失败'

        #创建weather表
        sql =\
            """create table weather(
                        city varchar(60) not null,
                        day_weath varchar(20),
                        day_wind varchar(30),
                        day_wind_power varchar(20),
                        day_temper varchar(10),
                        night_weath varchar(20),
                        night_wind varchar(30),
                        night_wind_power varchar(20),
                        night_temper varchar(10),
                        unique(city)
                        )character set utf8;"""

        try:
            self.cur.execute(sql)
            self.conn.commit()
            print('创建weather表成功')
        except Exception as e:
            self.conn.rollback()
            print('error:%s' % e)
            return '创建weather表失败'

        self.create_index()

    def create_index(self):
        '''
            创建表的索引关系
        '''
        #给client表的 id  car_plate增加索引
        sql_id = "alter table client add index id(id);"
        # sql_car_plate1 = "alter table client add index car_plate(car_plate);"

        #给login表的 username添加索引
        sql_username = "alter table login add index username(username);"

        #给history 的 car_plate添加索引
        sql_car_plate2 = "alter table history add index car_plate(car_plate);"

        sql_list = [sql_id,sql_username,sql_car_plate2]
        for sql in sql_list:
            try:
                self.cur.execute(sql)
                self.conn.commit()
                print('创建索引成功')
            except Exception as e:
                self.conn.rollback()
                print('error:%s' % e)
                return '创建索引失败'
        print('索引关系创建完成')
        
        self.init_carbarn()

    def init_carbarn(self):
        '''
            此函数用来初始化carbarn表，增加80个车位　　００１－－０８０
        '''
        for car_place in range(1,81):
            sql = "insert into carbarn(car_place) values(%d);" % car_place
            try:
                self.cur.execute(sql)
                self.conn.commit()
                # print(car_place,'插入成功')
            except Exception as e:
                self.coon.rollback()
                print('error:%s' % e)

        print('carbarn正常数据插入成功')

        #插入第８１条数据，用来解决client的car_place的外键关联carbarn的car_place字段
        #如果不是会员就没有车位，设置为null以供使用
        sql = "insert into carbarn(isStop,member) values(True, True);"
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print('error:%s' % e)

        self.close()



        


if __name__ == '__main__':
    client = Client('information_schema','CarBarntest2')
    client.create_database()



