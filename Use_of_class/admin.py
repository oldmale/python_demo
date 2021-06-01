#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/27 16:25
# @Author  : Puxf
# @Site    : 
# @File    : admin.py
# @Software: PyCharm

class Admin(User):
    """继承管理员"""
    def __init__(self,first_name,last_name,age):
        """初始化父类属性"""
        super().__init__(first_name,last_name,age)
        """初始化用户权限特有属性"""
        self.privileges = Privileges()


    def show_privileges(self,*privileges):
        self.privileges = list(privileges)
        print("用户名：" + self.first_name + self.last_name +
              "\n你的权限有：")
        for i in self.privileges:
            print(i)