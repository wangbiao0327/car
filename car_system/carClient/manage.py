'''
这是一个车库管理系统的管理模块，用来管理车库的停车，取车功能

Author: Recall
Date:   2018-10-13
module: socket、os
Email:
'''


from socket import *
import os

sock_file = '/home/tarena/car_system2.0/car_system/carServer/sock_file'

class Manage(object):
    def __init__(self):
        self.sock = socket(AF_UNIX,SOCK_STREAM)
        self.sock.connect(sock_file)
        self.sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

    def park(self,plate):
        '''
        此类函数用来做停车功能使用

        参数：车牌
        功能:判断能否停车
        返回值：
            可以停车：[True,车位号,取车码]
            不能停车：[False]
        '''
        data = 'park  %s' % plate
        self.sock.send(data.encode())
        # car_jude = True #此处模拟车牌号识别，判断是否符合停放要求
        aff_list = self.sock.recv(1024).decode().split("  ")
        if aff_list[0] == "ok":
            return [True,aff_list[1],aff_list[2]]
        return [False]

    def get_car(self,plate,take_car):
        '''
        此函数用来做取车功能

        参数：车牌号，取车码
        返回值：
            成功：[True]
            失败：[False,错误原因]
        '''
        data = 'get_car  %s  %s' % (plate,take_car)
        self.sock.send(data.encode())
        aff = self.sock.recv(1024).decode().split("  ")
        if aff[0] != "ok":
            return [False,aff[0]]
        return [True,aff[1]]

print(__name__)
if __name__ == '__main__':
    admin = Manage()
    while True:
        choise = input("请输入选择")
        if choise == '1':
            plate = input("车牌")
            print(admin.park(plate))
        else:
            plate = input("车牌")
            take_car = input("取车码")
            print(admin.get_car(plate,take_car))