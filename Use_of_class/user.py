#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/27 16:26
# @Author  : Puxf
# @Site    : 
# @File    : user.py
# @Software: PyCharm

"""一个可用于表示用户信息的类"""

class User():
    """用户信息"""
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0
    def describe_user(self):
        """打印用户信息摘要"""
        print("姓："+self.first_name+" "+"名："+
              self.last_name +" "+ "年龄："+ str(self.age) + " "
              "登录次数："+str(self.login_attempts))
    def greet_user(self,original="你好！"):
        """向用户显示问候语"""
        print(self.first_name + self.last_name + " "+ original)

    def increment_login_attempts(self):
        """将属性login_attempts值加1"""
        self.login_attempts += 1
    def reset_login_attempts(self):
        """重置属性login_attempts为0"""
        self.login_attempts = 0