#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/28 17:03
# @Author  : Puxf
# @Site    : 
# @File    : store_data.py
# @Software: PyCharm


import json

# numbers = [1,2,4,5,2,21,321,312,32,123,2345]
# filename = 'numbers.json'
# with open(filename,'w') as f:
#     json.dump(numbers,f)

# filename = 'numbers.json'
# with open(filename) as f:
#     numbers = json.load(f)
#     print(numbers)


# name = input("请输入名字：")
# filename = 'name.json'
# with open(filename,'w') as f:
#     json.dump(name,f)
# print(name)

# filename = 'name.json'
# with open(filename) as f:
#     names = json.load(f)
# print('Hello',names)

# filename = 'name.json'
# try:
#     with open(filename) as f:
#         username = json.load(f)
# except FileNotFoundError:
#     username = input("请输入名字：")
#     with open(filename,'w') as f:
#         json.dump(username,f)
#         print('Hello,'+ username)
# else:
#     print('Hello,'+ username)




"""10-11 喜欢的数字：编写一个程序，提示用户输入他喜欢的数字，并使用
json.dump()将这个数字存储到文件中。再编写一个程序，从文件中读取这个值，并打
印消息“I know your favorite number! It’s _____.”。"""

# filename = 'numbers.json'
#
# # while True:
# #     tips = input('请输入一个你喜欢的数字或者"q"退出：')
# #     if tips == 'q':
# #         break
# #     with open(filename,'w') as f:
# #         json.dump(tips,f)
# #     print('你喜欢的数字是：',tips)
#
#
# with open(filename) as f:
#     nums = json.load(f)
#     print('我喜欢的数字是：',nums)



