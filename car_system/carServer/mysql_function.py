'''此模块编写CarBarn库里４个表的实体类，通过这个类对应的对象可以对该表进行增删改查操作
'''

from  pymysql import connect
import requests,time
from bs4 import BeautifulSoup

#此函数执行sql的增删改语句，传入db,cur,sql,正常执行返回True,异常返回 [False,error]
def do_sql(conn,cur,sql):
    cur.execute(sql)
    conn.commit()
    return [True]

#此函数执行mysql的查找,返回列表
def do_select_sql(conn,cur,sql):
    cur.execute(sql)
    conn.commit()
    result = []
    results = cur.fetchall()
    for re in results:
        print('re',re)
        result.append(list(re))
    # print('result',result)
    if not result:
        return [False]
    return [True]+result



class Client_function(object):
    def __init__(self,host="localhost",db='CarBarntest2',
             user="root",password="123456",
             charset="utf8",port=3306):
        self.database = db
        self.host = host
        self.user = user 
        self.password = password
        self.charset = charset
        self.port = port
        self.open()

    def open(self):
        # 创建conn
        self.conn = connect(host=self.host,
                user=self.user,password=self.password,
                database=self.database,
                charset=self.charset,
                port=self.port)
        # 创建游标cur
        self.cur = self.conn.cursor()

        #进入CarBarn数据库
        try:
            self.cur.execute("use %s;" % self.database)
            self.conn.commit()
            print('进入数据库成功')
        except Exception as e:
            self.conn.rollback()
            print("error:%s" % e)


    # 关闭
    def close(self):
        self.cur.close()
        self.conn.close()

    #增加普通人员
    def add_genral_user(self,username,phone_number,\
            car_factory,car_model,car_color,\
            car_plate):
        sql = "insert into client(name,username,phone_number,car_factory,car_model,car_color,car_plate) values('%s','%s','%s','%s','%s','%s','%s');"%(\
                                    username,username,phone_number,car_factory,car_model,\
                                    car_color,car_plate)
        print(sql)
        result = do_sql(self.conn,self.cur,sql)
        if result[0]:
            print('插入普通用户成功')
            return [True]
        else:
            print('error:%s' % result[-1])
            return [False,result[-1]]

    #增加会员
    def add_member_user(self,username,phone_number,\
            car_factory,car_model,car_color,\
            car_plate,car_place,member):
        sql = "insert into client(name,username,phone_number,car_factory,car_model,car_color,car_plate,car_place,member) values('%s','%s','%s','%s','%s','%s','%s',%d,%s);"%(\
                                    username,username,phone_number,car_factory,car_model,\
                                    car_color,car_plate,car_place,member)
        print(sql)
        result = do_sql(self.conn,self.cur,sql)
        if result[0]:
            print('插入会员用户成功')
            return [True]
        else:
            print('error:%s' % result[-1])
            return [False,result[-1]]

    #删除用户,传入用户名
    def delete_user(self,username):
        sql = "delete from client where username = '%s';" % username
        print(sql)
        result = do_sql(self.conn,self.cur,sql)
        if result[0]:
            print("删除成功")
            return result
        else:
            print('error:%s' % result[-1])
            return False

    #通过username查找用户信息
    def select_user_by_username(self,username):
        sql = "select * from client where username = '%s';" % username
        print(sql)
        result = do_select_sql(self.conn,self.cur,sql)
        if result[0]:
            print('查找成功')
            print(result)
            return result
        else:
            print(result)
            print('error:%s' % result[-1])
            return result

    #通过id查找用户信息
    def select_user_by_id(self,id):
        sql = "select * from client where id=%d;" % id
        print(sql)
        result = do_select_sql(self.conn,self.cur,sql)
        if result[0]:
            print('查找成功')
            print(result)
            return result
        else:
            print('error:%s' % result[-1])
            return result

    # 通过plate查找用户信息
    def select_user_by_plate(self, plate):
        sql = "select * from client where car_plate='%s';" % plate
        print(sql)
        result = do_select_sql(self.conn, self.cur, sql)
        if result[0]:
            print('查找成功')
            print(result)
            return result
        else:
            print('error:%s' % result[-1])
            return result

    #修改信息，暂时只提供修改用户名,需要传入id和 新的username
    def modify_username(self,id,username):
        sql = "update client set username='%s' where id=%d;" % (username,id)
        result = do_sql(self.conn,self.cur,sql)
        if result[0]:
            print("修改成功")
            return True
        else:
            print('error:%s' % result[-1])
            return False

    def modify_user_phone(self,username,phone):
        sql = "update client set phone_number='%s' where username='%s;" % (phone,username)
        print("msg",sql)
        result = do_sql(self.conn, self.cur, sql)
        if result[0]:
            print("修改成功")
            return True
        else:
            print('error:%s' % result[-1])
            return False


class Login_fuction(object):
    def __init__(self,host="localhost",db='CarBarntest2',
             user="root",password="123456",
             charset="utf8",port=3306):
        self.database = db
        self.host = host
        self.user = user 
        self.password = password
        self.charset = charset
        self.port = port
        self.open()

    def open(self):
        # 创建conn
        self.conn = connect(host=self.host,
                user=self.user,password=self.password,
                database=self.database,
                charset=self.charset,
                port=self.port)
        # 创建游标cur
        self.cur = self.conn.cursor()

        #进入CarBarn数据库
        try:
            self.cur.execute("use %s;" % self.database)
            self.conn.commit()
            print('进入数据库成功')
        except Exception as e:
            self.conn.rollback()
            print("error:%s" % e)


    # 关闭
    def close(self):
        self.cur.close()
        self.conn.close()

    #增加用户,传入id,username,password,email,默认不再登录状态
    def add_user(self,id,username,password,email):
        sql = "insert into login(id,username,password,email,isLogin) values(%d,'%s','%s','%s','False');" % (id,username,\
                                                                                        password,email)
        result = do_sql(self.conn,self.cur,sql)
        if result[0]:
            print("添加login用户成功")
        else:
            print('error:%s' % result[-1])
        return result

    def modify_username(self,id,new_username):
        '''
            修改login表的username字段
            参数：用户id　和　新的用户名
            返回值：布尔值，True表示修改成功，False表示修改失败
        '''
        sql = "update login set username='%s' where id=%d;" % (new_username,id)
        result = do_sql(self.conn,self.cur,sql)
        if result[0]:
            print("用户名修改成功")
        else:
            print("error:%s" % result[-1])
        return result

    def modify_password(self,username,new_password):
        '''
            此函数用于修改用户的登录密码
            参数：username,password
            返回值：布尔值，TRue表示修改成功，False表示修改失败


        '''
        sql = "update login set password='%s' where username='%s';" % (new_password,username)
        result = do_sql(self.conn,self.cur,sql)
        if result[0]:
            print('密码修改成功')
        else:
            print('error:%s' % result[-1])
        return result

    def modify_email(self,username,new_email):
        '''
            此函数修改login表的username
            传入参数：用户名：username  和　　新邮箱new_email
            返回值：
                布尔值，True表示修改成功，False表示修改失败
        '''
        sql = "update login set email='%s' where username='%s';" % (new_email,username)
        result = do_sql(self.conn,self.cur,sql)
        if result[0]:
            print('邮箱修改成功')
        else:
            print('error:%s' % result[-1])
        return result

    #修改user的登录状态,传入username和　　要设置的状态  True  False
    def modify_login_status(self,username,status):
        sql = "update login set isLogin='%s' where username='%s';" % (status,username)
        print(sql)
        result = do_sql(self.conn,self.cur,sql)
        if result[0]:
            print('修改成功')
        else:
            print('error:%s' % result[-1])
        return result

    def modify_active_status(self,username,status):
        '''
        是否允许用户的登录,更改isActive的值，True表示允许登录，False表示不允许登录
        传入用户名username和状态status

        '''
        sql = "update login set isActive='%s' where username='%s';" % (status,username)
        result = do_sql(self.conn,self.cur,sql)
        if result[0]:
            print('修改状态成功')
        else:
            print("error:%s" % result[-1])
        return result

    def select_user_information(self,username):
        '''
            此函数用于查取login表的数据
            传入参数：
                用户名：username
            返回值：
                列表
                查找成功  [True,[该用户的记录],[],...]
                查找失败  [False]
        '''
        sql = "select * from login where username='%s';" % username
        print(sql)
        result = do_select_sql(self.conn,self.cur,sql)
        if result[0]:
            print('查找成功')
            for re in result[1:]:
                print(re)
            if len(result)<2:
                print("没有记录")
                return '没有结果'
        else:
            print('error:%s' % result[-1])
        return result

class Carbarn_function(object):
    """此类用来操作carbarn表"""
    def __init__(self,host="localhost",db='CarBarntest2',
             user="root",password="123456",
             charset="utf8",port=3306):
        self.database = db
        self.host = host
        self.user = user 
        self.password = password
        self.charset = charset
        self.port = port
        self.open()

    def open(self):
        # 创建conn
        self.conn = connect(host=self.host,
                user=self.user,password=self.password,
                database=self.database,
                charset=self.charset,
                port=self.port)
        # 创建游标cur
        self.cur = self.conn.cursor()

        #进入CarBarn数据库
        try:
            self.cur.execute("use %s;" % self.database)
            self.conn.commit()
            print('进入数据库成功')
        except Exception as e:
            self.conn.rollback()
            print("error:%s" % e)


    # 关闭
    def close(self):
        self.cur.close()
        self.conn.close()

    def select_car_place(self):
        '''
            此函数用于返回车位
            只要不是会员专用车位以及停了车的普通车位，都可以停车
            返回值：[True,car_place] 表示如果有车位，返回一个可用的车位
                　　　[False]表示没有车位了
        '''
        sql = "select * from carbarn where isStop='False' and member='False';"
        result = do_select_sql(self.conn,self.cur,sql)
        if result[0]:
            print(result[1][1])
            return [True,result[1][1]]

        else:
            print('error:%s' % result[-1])
        return result

    def stop_car(self,car_plate):
        '''
            此函数用于停车
            现根据车牌号去client表里查找是否是会员的车
            如果是返回此车位
            如果不是会员，去调用select_car_place，然后把此车存入carbarn表,同时改isStop的值为True
            返回这条记录
        '''
        sql = "select * from client where car_plate='%s' and member='True';" % car_plate
        result = do_select_sql(self.conn,self.cur,sql)
        print('++++++++++++++++++',result,'----------------------------------------------------')
        if result[0]:
            if result[1][-1]=="True":
                car_place = result[1][-2]
            else:
                car_place = self.select_car_place()[1]
        else:
            car_place = self.select_car_place()[1]
            print("不是会员的车位",car_place)
        #把car_plate　存入 car_place,插入当前时间，把isStop修改为True
        sql = "update carbarn set car_plate='%s',into_time=now(),isStop='True' where car_place='%s';" % (
                                                                                car_plate,car_place)
        result = do_sql(self.conn,self.cur,sql)
        if result[0]:
            print("停车成功")
            sql = "select * from carbarn where car_place = '%s';" % car_place
            results = do_select_sql(self.conn,self.cur,sql)
            print(results)
            return results[1]
        else:
            print("error:%s" % result[-1])
            return result

    def get_car(self,car_plate):
        '''
            此函数用于取车
            根据车牌号查询出记录，返回此条记录，并修改isStop的值为False,car_place修改为null
        '''

        #先根据车牌号查一下有没有停放此车,如果有正常操作，如果没有返回[False]
        sql = "select * from carbarn where car_plate='%s';" % car_plate
        result = do_select_sql(self.conn,self.cur,sql)
        if result[0] == True and len(result)>1:
            return result[1]
        return [False]
        #说明此车停放在车库
        #修改记录：包括修改isStop为False,car_plate为null,因为开始停车时间对操作无影响，不做修改，减少无意义的操作
        #获取记录
        stop_recording = result[1]#列表形式
        # sql = "update carbarn set car_plate=null,isStop='False' where car_plate='%s';" % car_plate
        # results = do_sql(self.conn,self.cur,sql)
        # if results[0]:
        #     print("取车成功")
        #     return stop_recording
        # else:
        #     print("error:%s" % results[-1])
        #     return [False]

    def update_car_is_stop(self,plate):
        sql = "update carbarn set car_plate=null,isStop='False' where car_plate='%s';" % plate
        results = do_sql(self.conn, self.cur, sql)

    def modify_isStop(self,car_place,status):
        '''
            修改此车位的isStop值，让此车位是否被查找到，能否停车
        '''
         #做修改
        sql = "update carbarn set isStop='%s' where car_place='%s';" % (status,car_place)
        result = do_sql(self.conn,self.cur,sql)
        if result[0]:
            return [True]
        else:
            return [False]

class History_function(object):
    def __init__(self,host="localhost",db='CarBarntest2',
             user="root",password="123456",
             charset="utf8",port=3306):
        self.database = db
        self.host = host
        self.user = user
        self.password = password
        self.charset = charset
        self.port = port
        self.open()

    def open(self):
        # 创建conn
        self.conn = connect(host=self.host,
                user=self.user,password=self.password,
                database=self.database,
                charset=self.charset,
                port=self.port)
        # 创建游标cur
        self.cur = self.conn.cursor()

        #进入CarBarn数据库
        try:
            self.cur.execute("use %s;" % self.database)
            self.conn.commit()
            print('进入数据库成功')
        except Exception as e:
            self.conn.rollback()
            print("error:%s" % e)


    # 关闭
    def close(self):
        self.cur.close()
        self.conn.close()

    def select_history_by_plat(self,plate,index=0):
        '''
        查询历史记录

        参数：车牌号，页数
        返回值：五条历史记录
        '''
        sql = '''
        select into_time,leave_time from history where car_plate = "%s" order by leave_time DESC limit %d,5;
        ''' % (plate,index)
        result = do_select_sql(self.conn,self.cur,sql)
        return result

    def delete_history(self):
        """
        删除历史记录

        参数：
        删除一个月以前的历史记录，并将删除的历史记录存入到history_log.txt文件中
        """
        sql_select = "select car_plate,into_time,leave_time from history where leave_time < (now() - interval 1 month)"
        result1 = do_select_sql(self.conn,self.cur,sql_select)
        with open("history_log.txt","w") as f:
            title = str(time.localtime()) + "\n"
            title += "车牌号".center(6) + "  "+"停车时间".center(15) + "  "+"离开时间".center(15) + "\n"
            f.write(title)
            for i in result1[1:]:
                f.write("%s  %s  %s\n" % (i[0],str(i[1]),str(i[2])))
        sql_delete = "delete from history where leave_time < (now() - interval 1 month)"
        result2 = do_sql(self.conn,self.cur,sql_delete)
        if result1[0] and result2[1]:
            return True
        return False

    def insert_history(self,plate):
        '''
        插入历史记录

        参数：　车牌号，进入时间
        返回值：［True］
        '''
        sql = '''insert into history select null,carbarn.car_plate,
                carbarn.into_time,now()
                 from carbarn where carbarn.car_plate='%s';''' % plate
        result = do_sql(self.conn,self.cur,sql)
        return result


class Weather_function(object):
    def __init__(self, host="localhost", db='CarBarntest2',
                 user="root", password="123456",
                 charset="utf8", port=3306):
        self.database = db
        self.host = host
        self.user = user
        self.password = password
        self.charset = charset
        self.port = port
        self.open()

    def open(self):
        # 创建conn
        self.conn = connect(host=self.host,
                            user=self.user, password=self.password,
                            database=self.database,
                            charset=self.charset,
                            port=self.port)
        # 创建游标cur
        self.cur = self.conn.cursor()

        # 进入CarBarn数据库
        try:
            self.cur.execute("use %s;" % self.database)
            self.conn.commit()
            print('进入数据库成功')
        except Exception as e:
            self.conn.rollback()
            print("error:%s" % e)

    # 关闭
    def close(self):
        self.cur.close()
        self.conn.close()

    def add_datas(self, city, day_weath, day_wind, day_wind_power,
                  day_temper, night_weath, night_wind, night_wind_power, night_temper):

        sql = "insert into weather(city,day_weath,day_wind,day_wind_power,\
        day_temper,night_weath,night_wind,night_wind_power,night_temper) values('%s','%s','%s','%s',\
        '%s','%s','%s','%s','%s');" % (city, day_weath, day_wind, day_wind_power,
                                       day_temper, night_weath, night_wind, night_wind_power, night_temper)

        result = do_sql(self.conn, self.cur, sql)
        if result[0]:
            print("数据插入成功")

    def select_weather(self, city):
        '''
            此函数用于查询城市天气
            参数：城市 city
            返回值：=城市对应的天气记录
        '''

        sql = "select * from weather where city='%s';" % city
        result = do_select_sql(self.conn, self.cur, sql)
        if result[0] == True and len(result) > 1:
            print("查询成功")
            print(result[1])
            return result
        else:
            print("error:%s" % result[-1])
            return result

    def delete_weather(self):
        '''
            此函数用于删除所有的表记录
        '''
        sql = "delete from weather;"
        result = do_sql(self.conn, self.cur, sql)
        if result[0]:
            print("删除记录成功")

        else:
            print("error:%s" % result[-1])

        return result

    def get_weather_pag(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        print('++++++++++++++++++++++++')
        if response.status_code == 200:
            soup = BeautifulSoup(response.content.decode("utf-8"), 'lxml')
            weathlist = soup.select('.conMidtab')[0].select('.conMidtab2')
            print(len(weathlist))
            return weathlist
        return None

    def get_city_weather(self, html):
        p_l = ["北京", '上海', '天津', '重庆']
        province = ''
        for table in html:
            for tr in table.select("tr")[2:]:
                print(province)
                if tr == table.select('tr')[2]:
                    province = tr.select("td")[0].text.split("\n")[1]
                    td_list = tr.select("td")[1:-1]
                else:
                    td_list = tr.select("td")[:-1]
                if province in p_l:
                    city = td_list[0].select('a')[0].text + '区'
                else:
                    city = td_list[0].select('a')[0].text + '市'
                d_weath = td_list[1].text
                d_wind = td_list[2].select("span")[0].text
                d_wind_power = td_list[2].select("span")[1].text
                d_temper = td_list[3].text

                n_weath = td_list[4].text
                n_wind = td_list[5].select("span")[0].text
                n_wind_power = td_list[5].select("span")[1].text
                n_temper = td_list[6].text
                self.add_datas( \
                    city, d_weath, d_wind, d_wind_power, d_temper, \
                    n_weath, n_wind, n_wind_power, n_temper)

    def add_data(self):
        '''
          此函数用与给weather表添加数据
      '''
        url_list = [
            "http://www.weather.com.cn/textFC/hb.shtml",
            'http://www.weather.com.cn/textFC/db.shtml',
            "http://www.weather.com.cn/textFC/hd.shtml",
            "http://www.weather.com.cn/textFC/hz.shtml",
            "http://www.weather.com.cn/textFC/hn.shtml",
            "http://www.weather.com.cn/textFC/xb.shtml",
            "http://www.weather.com.cn/textFC/xn.shtml"
        ]

        for i in url_list:
            html = self.get_weather_pag(i)
            if html:
                self.get_city_weather(html)
                time.sleep(1)









    



if __name__ == '__main__':
#测试client_function类
    # client_function = Client_function()
    #插入普通用户
    # client_function.add_genral_user('试验员五','17688893005','宝马','x3','红色','粤B.93005')
    #插入会员用户
    # client_function.add_member_user('试验员六','17688893006','宝马','x3','红色','粤B.93006',6,True)
    #删除用户
    # client_function.delete_user('试验员六')
    #通过username查找用户
    # client_function.select_user_by_username('试验员五')
    #通过id查找用户
    # client_function.select_user_by_id(1)
    #修改用户信息
    # client_function.modify_username(1,17688893659)

#测试login_function类
    login_function = Login_fuction()
    # login_function.add_user(1,'试验员一','qdd123456','458620786@qq.com')
    #测试修改登录状态
    # login_function.modify_login_status('试验员一',False)
    #修改用户是否被激活
    # login_function.modify_active_status('试验员四','True')
    #查看试验员一的信息
    # login_function.select_user_information('试验员2s')
    #修改试验员一的登录密码为qdd12345
    # login_function.modify_password('试验员一','qdd12345')
    #修改试验员二的用户名为试验员二二
    # login_function.modify_username(2,'试验员二二')
    #修改邮箱
    login_function.modify_email('试验员三','6666666@qq.com')