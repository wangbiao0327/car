#！user/bin/env python3.7
# coding:utf-8
# author:wanghongzhang
# email:458620786@qq.com
# time: 2018/11/20
import datetime
import sys


import pygame
import time

from PyQt5.QtCore import QVariant
from bai_du_voice import *

from Manage_mainwindow import Ui_Manage_UI
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5 import QtCore, QtGui, QtWidgets

from predict import *

from get_filename import get_files

from multiprocessing import Process
from threading import  Thread

from manage import *




def broadcast(t):
    # f = 'D:\PycharmProjects\car_system2.0\car_plate_voice.mp3'
    f = '/home/tarena/car_system2.0/car_plate_voice.mp3'
    pygame.mixer.init()
    track = pygame.mixer.music.load(f)
    pygame.mixer.music.play()
    time.sleep(t)
    pygame.mixer.music.stop()


def leave_broadcast():
    # f = 'D:\PycharmProjects\car_system2.0\car_plate_voice.mp3'
    f = '/home/tarena/car_system2.0/car_plate_voice.mp3'
    pygame.mixer.init()
    track = pygame.mixer.music.load(f)
    pygame.mixer.music.play()
    time.sleep(8)
    pygame.mixer.music.stop()

dic ={'key': 'values'}

def update_car_title(label, car):
    pass




class Manage_UI(Ui_Manage_UI):
    def __init__(self, manage_car_system):
        super(Manage_UI, self).__init__()
        self.mainwindow = QMainWindow()
        self.setupUi(self.mainwindow)
        self.mainwindow.show()
        self.click()
        self.c = CardPredictor()
        self.c.train_svm()
        self.manage_car_system = manage_car_system
        self.leave_combox_list = []
        self.leave_combox_dic={}
        self.index = 0
        self.i = 0

    def click(self):
        self.manage_stop_car_btn.clicked.connect(self.display)
        self.manage_leave_car_btn.clicked.connect(self.get_car)
        self.manage_stop_car_combox.addItem('请选择', QVariant(0))
        # FILE_PATH = 'D:\PycharmProjects\car_system2.0\car_plate_picture'
        FILE_PATH = '/home/tarena/car_system2.0/car_plate_picture'

        self.into_combox_list = get_files(FILE_PATH)
        self.update_into_combox()

    def update_into_combox(self):
        file_dict = {}
        self.file_dict_not ={}
        for index, fi in zip(range(len(self.into_combox_list)), self.into_combox_list):
            # print(index,fi[:-3])
            file_dict[index] = fi[:-3]
            self.file_dict_not[fi[:-3]] = index
        print("file_dict",file_dict)
        print("file_dict_not",self.file_dict_not)



        for key, values in file_dict.items():
            # print(values[:-1])
            self.manage_stop_car_combox.addItem(values[:-1], QVariant(int(key)))

    def display(self):
        #切换图片

        text = self.manage_stop_car_combox.currentText()
        text = text + '.jpg'
        try:
            r, roi, color = self.c.predict('car_plate_picture/'+text)
        except Exception as e:
            return
        print('车牌号',r)
        self.car_plate = ''
        for s in r:
            self.car_plate += s

        print("into_palte",self.car_plate)
        self.change_into_picture()
        self.update_car_titles()
        times = time.ctime().split(' ')[-2].split(':')
        sounds = "欢迎"+self.car_plate+"进入车库，现在时间是%s点%s分" % (times[0], times[1])
        self.get_voice(sounds)
        #存放进数据库
        self.into_car_barn()

    def test(self):
        #创建一个新的进程去显示是读出来的车牌号
        p2 = Thread(target=update_car_title, args=(self.manage_stop_car_display, self.car_plate,))
        p2.start()
        p2.join()


    def update_car_titles(self):
        car_plate_label = "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">" + self.car_plate + "</span></p></body></html>"
        self.manage_stop_car_display.setText(car_plate_label)

    def get_voice(self, sounds):
        token = fetch_token()
        # times = time.ctime().split(' ')[-2].split(':')
        # sounds = "欢迎"+self.car_plate+"进入车库，现在时间是%s点%s分" % (times[0], times[1])
        tex = quote_plus(sounds)  # 此处TEXT需要两次urlencode
        # print(tex)
        params = {'tok': token, 'tex': tex, 'per': PER, 'spd': SPD, 'pit': PIT, 'vol': VOL, 'aue': AUE, 'cuid': CUID,
                  'lan': 'zh', 'ctp': 1}  # lan ctp 固定参数

        data = urlencode(params)
        # print('test on Web Browser' + TTS_URL + '?' + data)
        #
        req = Request(TTS_URL, data.encode('utf-8'))

        has_error = False
        try:
            f = urlopen(req)
            car_plate_voice_str = f.read()

            has_error = ('Content-Type' not in f.headers.keys() or f.headers['Content-Type'].find('audio/') < 0)
        except  URLError as err:
            # print('asr http response http code : ' + str(err.code))
            car_plate_voice_str = err.read()
            has_error = True

        save_file = "error.txt" if has_error else 'car_plate_voice.' + FORMAT
        with open(save_file, 'wb') as of:
            of.write(car_plate_voice_str)
        #创建一个新的进程去播报
        # time.sleep(2)
        p = Process(target=broadcast, args=(5,))
        p.start()
        p.join()

    def change_into_picture(self):
        print(self.car_plate)
        self.dic_car_plates = {
            '京E51619':'car1_51619',
            '皖AUB816':'car2_ub816',
            '皖ATH859':'car3_th859',
            '皖A87271':'car4_87271', 
            '豫C66666':'car6_66666',
            '吉AA266G':'car7_a266g',
        }


        #刷新进车库下拉列表

        current_index = self.manage_stop_car_combox.currentIndex()
        self.manage_stop_car_combox.removeItem(current_index)
        #把停进来的车从入库列表中删除
        print("self.into_combox_list",self.into_combox_list)
        #把停进来的车牌号放到去车列表里面
        self.leave_combox_list.append(self.dic_car_plates[self.car_plate])
        self.Manage_into_car_picture.setStyleSheet("QGroupBox { background-image:url(:/new/prefix1/car_picture/"+self.dic_car_plates[self.car_plate]+".jpg)}")
        #刷新出库下拉列表
        self.update_leave_combox()
        self.default_into_image()

    def update_leave_combox(self):

        self.manage_leave_car_combox.addItem(self.dic_car_plates[self.car_plate], QVariant(int(self.index)))
        self.index += 1
        self.leave_combox_list = list(set(self.leave_combox_list))

    def get_car(self):
        '''
        此函数用于取车按钮按下后的操作
        '''
        #被选择出来的车从取车下拉列表中去除
        #获取下拉列表的当前值，用作增加到停车列表
        item = self.manage_leave_car_combox.currentText()
        index = self.manage_leave_car_combox.currentIndex()
        self.manage_leave_car_combox.removeItem(index)
        #添加到停车下拉列表
        self.manage_stop_car_combox.addItem(item)
        #背景图换成取出来的车的图片
        # item = self.manage_leave_car_combox.currentText()
        print(item)
        self.Manage_leave_car_picture.setStyleSheet(
            "QGroupBox { background-image:url(:/new/prefix1/car_picture/" +item+ ".jpg)}")
        self.leave_car_barn(item)

    def get_leave_voice(self, sounds):
        token = fetch_token()
        # times = time.ctime().split(' ')[-2].split(':')
        # sounds = "欢迎"+self.car_plate+"进入车库，现在时间是%s点%s分" % (times[0], times[1])
        tex = quote_plus(sounds)  # 此处TEXT需要两次urlencode
        # print(tex)
        params = {'tok': token, 'tex': tex, 'per': PER, 'spd': SPD, 'pit': PIT, 'vol': VOL, 'aue': AUE, 'cuid': CUID,
                  'lan': 'zh', 'ctp': 1}  # lan ctp 固定参数

        data = urlencode(params)
        # print('test on Web Browser' + TTS_URL + '?' + data)
        #
        req = Request(TTS_URL, data.encode('utf-8'))

        has_error = False
        try:
            f = urlopen(req)
            car_plate_voice_str = f.read()

            has_error = ('Content-Type' not in f.headers.keys() or f.headers['Content-Type'].find('audio/') < 0)
        except  URLError as err:
            # print('asr http response http code : ' + str(err.code))
            car_plate_voice_str = err.read()
            has_error = True

        save_file = "error.txt" if has_error else 'car_plate_voice.' + FORMAT
        with open(save_file, 'wb') as of:
            of.write(car_plate_voice_str)

        p = Process(target=leave_broadcast)
        p.start()
        p.join()

    def default_into_image(self):
        pass
                                                

    def into_car_barn(self):
        #存车
        car_plate = str(self.car_plate)
        car_plate = car_plate[0:2] + '.' + car_plate[2:]
        result = self.manage_car_system.park(car_plate)
        if result[0]:
            self.stop_car = [result[1], result[2]]
        else:
            return 

        # "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">" + self.car_plate + "</span></p></body></html>"
        
        html = "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">" +result[2]+"</span></p></body></html>"
        self.manage_stop_car_code_value_label.setText(html)
        print(result)

    def leave_car_barn(self,text):
        # text = self.manage_leave_car_combox.currentText()
        text = text + '.jpg'
        print(text)
        try:
            r, roi, color = self.c.predict('car_plate_picture/'+text)
        except Exception as e:
            return
        car_plate = ''
        for s in r:
            car_plate += s
        plate = car_plate
        car_plate = car_plate[0:2] + '.' + car_plate[2:]
        print(self.stop_car[0], self.stop_car[1])
        stop_code = self.manage_leave_input_stop_car_code_edit.text().strip()
        print("从标签取出的验证码", stop_code)
        result = self.manage_car_system.get_car(car_plate, stop_code)
        if result[0]:
            html = "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">" + result[1] +"</span></p></body></html>"
            self.manage_stop_money_label.setText(html)
            print(result)
            
            print("leave_plate",car_plate)
            
            sounds = plate+"离开车库，收费%s元,感谢您使用爱停车系统,祝您生活愉快" % result[1]
            self.get_leave_voice(sounds)
        else:
            print("驱车失败")
            return
           

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #创建manage对象，
    manage_car_system = Manage()
    manage = Manage_UI(manage_car_system)
    sys.exit(app.exec_())