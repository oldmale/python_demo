#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/26 13:50
# @Author  : Puxf
# @Site    : 
# @File    : one.py
# @Software: PyCharm


# class Dog():
#     """一次模拟小狗的简单尝试"""
#
#     def __init__(self,name,age):
#         """初始化属性name和age"""
#         self.name = name
#         self.age = age
#     def sit(self):
#         """模拟小狗被命令时蹲下"""
#         print(self.name,"开始蹲下")
#     def roll_over(self):
#         """模拟小狗被命令时打滚"""
#         print(self.name,"开始打滚")
# my_dog = Dog('wihell',6)
# my_dog.sit()
# my_dog.roll_over()



# class Restaurant():
#     """一次模拟餐馆营业状态的尝试"""
#
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#     def describe_restaurant(self):
#         """餐馆名和菜肴类型"""
#         print(self.restaurant_name,self.cuisine_type)
#     def get_number(self):
#         print('已经有',str(self.number_served),'人就餐')
#     def set_number_seived(self,number):
#         self.number_served = number
#
#
#     def open_restaurant(self):
#         """餐馆正在营业"""
#         print(self.restaurant_name,"----- 正在营业")
#
#     def increment_number_served(self,aoto):
#         self.number_served += aoto
#         return self.number_served
# #创建实例
# restaurant = Restaurant('谷田稻香','川菜')
# restaurant.set_number_seived(15)
# restaurant.get_number()
# restaurant.increment_number_served(-8)
# restaurant.get_number()


# my_ra = Restaurant('谷田稻香','川菜')
# my_ra1 = Restaurant('辛湘汇','湘菜')
# my_ra2 = Restaurant('肯德基','汉堡')
# my_ra.describe_restaurant()
# my_ra1.describe_restaurant()
# my_ra2.describe_restaurant()


# class User():
#     """用户属性初始化"""
#     def __init__(self,first_name,last_name,age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.login_attempts =0
#
#     def describe_user(self):
#         """打印用户信息摘要"""
#
#         print(self.first_name + self.last_name,self.age + "岁了","登陆次数：",self.login_attempts)
#
#     def greet_user(self,count="你好！"):
#         """向用户问好"""
#         print(self.first_name + self.last_name,count)
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#
#
#     def reset_login_attempts(self):
#             self.login_attempts = 0
#
#
#
# one = User('du','wangjun','23')
# one.describe_user()
# one.increment_login_attempts()
# one.describe_user()
# one.reset_login_attempts()
# one.describe_user()

#
# one = User('杜','飞','8')
# one.describe_user()
# one.greet_user('萨瓦迪卡')


# class User():
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.login_attempts = 0
#
#     def describe_user(self):
#         print(self.first_name.title() + " " + self.last_name.title())
#
#     def greet_user(self):
#         print("Hello " + self.first_name.title() + " " + self.last_name.title())
#
#     def login_attempts_number(self):
#         print("You have tried " + str(self.login_attempts) + " times !")
#
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#
#
# VIP = User('yun', 'mengze')
# VIP.describe_user()
# VIP.greet_user()
# for n in range(10):
#     VIP.increment_login_attempts()
#
# VIP.login_attempts_number()
# VIP.reset_login_attempts()
# VIP.login_attempts_number()


floas = []
a = ('苹果','草莓','西瓜')
floas = list(a)
for i in floas:
    print(i)
print(floas)



