#！user/bin/env python3.7
# coding:utf-8
# author:wanghongzhang
# email:458620786@qq.com
# time: 2018/11/20


import os

def get_files(FILE_PATH):
    file_list = os.listdir(FILE_PATH)
    # print(file_list)
    files =[]
    for file in file_list:
        if file[0] != '.':
            files.append(file)
    return files

    # file_dict={}
    # for index,fi in zip(range(len(files)),files):
    #     # print(index,fi[:-3])
    #     file_dict[index] = fi[:-3]
    #
    # return  file_dict





# FILE_PATH = 'D:\PycharmProjects\car_system2.0'
#
# print(get_files(FILE_PATH))

