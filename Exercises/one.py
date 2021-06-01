#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/24 11:11
# @Author  : Puxf
# @Site    : 
# @File    : one.py
# @Software: PyCharm


#变量
# name = 'Jake'
#name是一个变量，name是变量名，Jake是值
#print(name.title()) #title()函数以首写字母大写
# print(name.upper())#upper()全部字母大写
# print(name.lower())#lower()全部小写

# /t制表符
# /n换行符
# /t/n指标并换行

#rstrip()去除末尾空白符
#lstrip()去除首部空白符
#strip()去除全部空白符


'''列表'''


"""请尝试编写一些简短的程序来完成下面的练习，以获得一些使用 Python 列表的第
一手经验。你可能需要为每章的练习创建一个文件夹，以整洁有序的方式存储为完成各
章的练习而编写的程序。
3-1 姓名：将一些朋友的姓名存储在一个列表中，并将其命名为 names。依次访问
该列表中的每个元素，从而将每个朋友的姓名都打印出来。
3-2 问候语：继续使用练习 3-1 中的列表，但不打印每个朋友的姓名，而为每人打
印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
3-3 自己的列表：想想你喜欢的通勤方式，如骑摩托车或开汽车，并创建一个包含
多种通勤方式的列表。根据该列表打印一系列有关这些通勤方式的宣言，如“I would like 
to own a Honda motorcycle”。"""


#3-1

# names = ['xiaodong','zhangdhi','wanghai']

# print(names[0])
# print(names[1])
# print(names[2])

#3-2

# wenhouyu = 'How are you'
# print(names[0] +' '+ wenhouyu)
# print(names[1] +' '+ wenhouyu)
# print(names[2] +' '+ wenhouyu)

#3-3
# mode = ['car','metro','aircraft','ship']
# mode1 = 'I like ' + mode[0]
# mode2 = 'I like ' + mode[1]
# mode3 = 'I like ' + mode[2]
# print(mode1,'\n'+ mode2,'\n'+mode3)



"""下面的练习比第 2 章的练习要复杂些，但让你有机会以前面介绍过的各种方式使用列表。
3-4 嘉宾名单：如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的），
你会邀请哪些人？请创建一个列表，其中包含至少 3 个你想邀请的人；然后，使用这个
列表打印消息，邀请这些人来与你共进晚餐。
3-5 修改嘉宾名单：你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。
 以完成练习 3-4 时编写的程序为基础，在程序末尾添加一条 print 语句，指出哪
位嘉宾无法赴约。
 修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
 再次打印一系列消息，向名单中的每位嘉宾发出邀请。
3-6 添加嘉宾：你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀
请哪三位嘉宾。
 以完成练习 3-4 或练习 3-5 时编写的程序为基础，在程序末尾添加一条 print 语
句，指出你找到了一个更大的餐桌。
 使用 insert()将一位新嘉宾添加到名单开头。
"""

#3-4
# name = ['xiaoming','xiaobai','xiaohong']
# name.append('yangyuan')
# name.append('gongjun')
# name[1] = 'wanghai'
# name.insert(0,'sunbing')

# print(name.pop())
# print(name.pop())
# print(name.pop())


#排序

# a = [4,5,7,2423,66,678,43,-98]
# # a.sort()
# a.reverse()
# # print(sorted(a))
# print(a)

# a = ['beijing','shanghai','xinjiang','qingdao','yunnan']
# # print(a)
# print(sorted(a))
# # print(a)
# b = sorted(a)
# b.reverse()
# print(b)




#列表操作
# a = []
# for i in range(1,6):
#
#     a.append(i*2)
# print(a)
#
# c = [i ** 2 for i in range(1,6)]
# b = list(range(1,6))
# print(b)



alien_color = 'red'

# if alien_color == 'green':
#     print('恭喜你获得五个点')
# elif alien_color == 'yello':
#     print('很遗憾')
# elif alien_color == 'red':
#     print('很一遗憾')

# names = ['admin','a','b','c','d']
# for i in names:
#     print('Hello ',i)
# a = 'a'
# if a == 'admin':
#     print('Hello admin, would you like to see a status report?')
# else:
#     print('d')
# a = input('请输入用户名：')
# if a == 'admin':
#     print('欢迎登陆')
# else:
#     print('抱歉，您输入的用户名不正确！')

#
# a = ['A','b','C','D','E']
# b = ['B','F','J','C','H']
# for i in b:
#     if i.lower() in a:
#         print(i+'用户名已被使用')
#     else:
#         print(i+'用户名未被使用')


# a = '\n请输入你的年龄：'
# a += '\n或者输入quit：'
# while True:
#     age = input(a)
#     if age == 'quit':
#         break
#     else:
#         age = int(age)
#         if age < 3:
#             print('票价：免费')
#         elif age >=3 and age <= 12:
#             print('票价：10美元')
#         else:
#             print('票价：15美元')
#

# prompt = "\nPlease enter the your age:"
# prompt += "\n(Enter 'quit' when you are finished.) "
# active=True
# while active :
#   age = input(prompt)
#   if age == 'quit':
#     active=False
#   else:
#       age=int(age)
#       if age<3:
#           print("free")
#       elif (age>=3 and age<=12):
#           print("The ticket price is 10 dollars.")
#       else:
#           print("The ticket price is 15 dollars.")

# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print("Verifying user: " + current_user.title())
#     confirmed_users.append(current_user)
#     # 显示所有已验证的用户
#     print("\nThe following users have been confirmed:")
#     for confirmed_user in confirmed_users:
#         print(confirmed_user.title())



name = ['sjij']
if name:
    print('不是空的')
else:
    print('kong')