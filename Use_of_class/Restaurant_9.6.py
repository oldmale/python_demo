#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/26 16:17
# @Author  : Puxf
# @Site    : 
# @File    : two.py
# @Software: PyCharm



"""9-1 餐馆：创建一个名为 Restaurant 的类，其方法__init__()设置两个属性：
restaurant_name 和 cuisine_type。创建一个名为 describe_restaurant()的方法和一个
名为 open_restaurant()的方法，其中前者打印前述两项信息，而后者打印一条消息，
指出餐馆正在营业。
根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述
两个方法。"""


# class Restaurant():
#     """模拟餐馆营业状态的实验"""
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         """显示餐馆两项信息"""
#         print("餐馆名："+ self.restaurant_name , "菜肴类型：" +self.cuisine_type)
#
#     def open_restaurant(self):
#         """显示餐馆正在营业"""
#         print(self.restaurant_name + "---正在营业中---")
#
# restaurant = Restaurant('辛湘阁','湘菜')
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

"""9-4 就餐人数：在为完成练习 9-1 而编写的程序中，添加一个名为 number_served
的属性，并将其默认值设置为 0。根据这个类创建一个名为 restaurant 的实例；打印有
多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
添加一个名为 set_number_served()的方法，它让你能够设置就餐人数。调用这个
方法并向它传递一个值，然后再次打印这个值。
添加一个名为 increment_number_served()的方法，它让你能够将就餐人数递增。
调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。"""

class Restaurant():
    """模拟餐馆营业状态的实验"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 50

    def describe_restaurant(self):
        """显示餐馆两项信息"""
        print("店名："+ self.restaurant_name , "店类型：" +
              self.cuisine_type+" " + "就餐人数："+str(self.number_served)+"人" )

    def open_restaurant(self):
        """显示餐馆正在营业"""
        print(self.restaurant_name + "---正在营业中---")
    def display_number(self):
        """显示有多少人在餐馆就餐过"""
        print("有",str(self.number_served),"人在",self.restaurant_name,"就餐过")
    def set_number_served(self,number):
        """设置就餐人数"""
        self.number_served = number
    def increment_number_served(self,numbes):
        total = self.number_served + numbes
        total1 = 28
        if total >= total1:
            print("现在里面位置坐满了，请稍等一会儿！")
        else:
            now = total1 - total
            print("现在有"+ str(total) + "人在就餐，还有"+str(now)+"个位置的")





# restaurant = Restaurant('辛湘阁','湘菜')
# restaurant.describe_restaurant()
# #restaurant.open_restaurant()
# restaurant.set_number_served(4)
# restaurant.increment_number_served(24)
# restaurant.display_number()



"""9-6 冰淇淋小店：冰淇淋小店是一种特殊的餐馆。编写一个名为 IceCreamStand 的
类，让它继承你为完成练习 9-1 或练习 9-4 而编写的 Restaurant 类。这两个版本的
Restaurant 类都可以，挑选你更喜欢的那个即可。添加一个名为 flavors 的属性，用于
存储一个由各种口味的冰淇淋组成的列表。编写一个显示这些冰淇淋的方法。创建一个
IceCreamStand 实例，并调用这个方法。"""

class IceCreaStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = []
    def increase_flavors(self,*flavor):
        self.flavors = list(flavor)
        print("\n店里的冰淇淋有以下几种口味：")
        for i in self.flavors:
            print(i)









I = IceCreaStand('小心心','冰淇淋')
"""describe_restaurant
open_restaurant
display_number
set_number_served
increment_number_served
"""
I.describe_restaurant()
I.increase_flavors('草莓','西瓜','苹果')

# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type):
#         #self.属性 的作用获取形参restaurant_name的值，并存储到restaurant_name中
#         #以供实例使用
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 20
#
#     def set_number_served(self,set_number):
#         #使用方法设置number_served属性的值
#         self.number_served = set_number
#
#     def increment_number_served(self,increment_number):
#         self.number_served += increment_number
#
#     def describe_restaurant(self):
#         print('您所在的餐厅是：' + self.restaurant_name +
#               ',餐饮类型是：' + self.cuisine_type +
#               ',就餐人数为：' + str(self.number_served) +
#               '人')
#
#     def open_restaurant(self):
#         print('餐厅正在营业！')
#
# class IceCreamStand(Restaurant):
#
#     def __init__(self,restaurant_name,cuisine_type):
#         super().__init__(restaurant_name,cuisine_type)
#         #给子类设置新的属性
#         self.flavors = ['草莓味','苹果味','原味奶油']
#
#     def describe_icecream(self):
#         print('\n本店提供的冰激凌有' + '3种:')
#         for show_flavors in self.flavors:
#             print(show_flavors)
# #9-6 冰淇淋小店
# my_icecream = IceCreamStand('梦想之家','冰激凌')
# my_icecream.set_number_served(15)
# my_icecream.increment_number_served(35)
# my_icecream.describe_restaurant()
# my_icecream.describe_icecream()
