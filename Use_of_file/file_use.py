#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/27 17:34
# @Author  : Puxf
# @Site    : 
# @File    : file_use.py
# @Software: PyCharm

"""10-3 访客：编写一个程序，提示用户输入其名字；用户作出响应后，将其名字写
入到文件 guest.txt 中。"""
# with open('name.txt','w') as f:
#     while True:
#         messg = input("请输入你的名字或者(q)退出：")
#         if messg == 'q':
#             break
#         print("How are you"+" "+messg)
#         f.write("How are you" + " " + messg + "\n")


"""10-5 关于编程的调查：编写一个 while 循环，询问用户为何喜欢编程。每当用户输
入一个原因后，都将其添加到一个存储所有原因的文件中。"""

with open('name.txt','w') as f:
    while True:
        message = input("请问你为什么喜欢编程或者输入(q)退出：")
        if message == 'q':
            break
        f.write("请问你为什么喜欢编程："+ message + "\n")




