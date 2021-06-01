#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/27 11:10
# @Author  : Puxf
# @Site    : 
# @File    : 9-7 Admin.py
# @Software: PyCharm



"""9-7 管理员：管理员是一种特殊的用户。编写一个名为 Admin 的类，让它继承你为
完成练习 9-3 或练习 9-5 而编写的 User 类。添加一个名为 privileges 的属性，用于存
储一个由字符串（如"can add post"、"can delete post"、"can ban user"等）组成的
列表。编写一个名为 show_privileges()的方法，它显示管理员的权限。创建一个 Admin
实例，并调用这个方法。"""



"""9-3 用户：创建一个名为 User 的类，其中包含属性 first_name 和 last_name，还有
用户简介通常会存储的其他几个属性。在类 User 中定义一个名为 describe_user()的方
法，它打印用户信息摘要；再定义一个名为 greet_user()的方法，它向用户发出个性化
的问候。
创建多个表示不同用户的实例，并对每个实例都调用上述两个方法"""

# class User():
#     """用户信息"""
#     def __init__(self,first_name,last_name,age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#     def describe_user(self):
#         """打印用户信息摘要"""
#         print("姓："+self.first_name+" "+"名："+
#               self.last_name +" "+ "年龄："+ str(self.age))
#     def greet_user(self,original="你好！"):
#         print(self.first_name + self.last_name + " "+ original)


# user1 = User('蒲','橙','23')
# user1.describe_user()
# user1.greet_user()



"""9-5 尝试登录次数：在为完成练习 9-3 而编写的 User 类中，添加一个名为
login_attempts 的属性。编写一个名为 increment_login_attempts()的方法，它将属性
login_attempts 的值加 1。再编写一个名为 reset_login_attempts()的方法，它将属性
login_attempts 的值重置为 0。
根据 User 类创建一个实例，再调用方法 increment_login_attempts()多次。打印属
性 login_attempts 的值，确认它被正确地递增；然后，调用方法 reset_login_attempts()，
并再次打印属性 login_attempts 的值，确认它被重置为 0。"""

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
# user1 = User('蒲','橙','23')
# user1.describe_user()
# user1.increment_login_attempts()
# user1.describe_user()
# user1.increment_login_attempts()
# user1.describe_user()
# user1.reset_login_attempts()
# user1.describe_user()



"""9-7 管理员：管理员是一种特殊的用户。编写一个名为 Admin 的类，让它继承你为
完成练习 9-3 或练习 9-5 而编写的 User 类。添加一个名为 privileges 的属性，用于存
储一个由字符串（如"can add post"、"can delete post"、"can ban user"等）组成的
列表。编写一个名为 show_privileges()的方法，它显示管理员的权限。创建一个 Admin
实例，并调用这个方法。"""


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



# Admin = Admin('刘','飞','23')
# Admin.show_privileges('可以禁止删除','可以添加帖子')


"""9-8 权限：编写一个名为 Privileges 的类，它只有一个属性——privileges，其中
存储了练习 9-7 所说的字符串列表。将方法 show_privileges()移到这个类中。在 Admin
类中，将一个 Privileges 实例用作其属性。创建一个 Admin 实例，并使用方法
show_privileges()来显示其权限。"""

class Privileges():
    def __init__(self,privileges=[]):
        self.privileges = ['修改','删除','添加']

    def show_privileges(self):
        print("你的权限有：")
        for i in self.privileges:
            print(i)


user1 = Admin('普','飞','23')
user1.privileges.show_privileges()




