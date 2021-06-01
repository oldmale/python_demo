#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/25 09:54
# @Author  : Puxf
# @Site    : 
# @File    : two.py
# @Software: PyCharm



# name = ['admin','jake','basw','hong','show']
# name_1 = ['JAKE','gour','hong','klow','rgor']
#
# for i in name_1:
#     if i.lower() in name:
#         print(i+ '用户名已被使用')
#     else:
#         print(i+ '用户名未被使用')

# number = list(range(1,10))
# for i in number:
#     if i == 1:
#         print('1st')
#     elif i == 2:
#         print('2nd')
#     elif i == 3:
#         print('3rd')
#     else:
#          print(str(i)+'th')

# ask = '请输入一个数字：'
# ask += '\n或者输入quit退出'
# asks = ''
# while asks != 'quit':
#     asks = input(ask)
#     if asks != 'quit':
#         print(asks)

# active = True
# while active:
#     asks = input(ask)
#     if asks == 'quit':
#         active = False
#     else:
#         print(asks)


age = '请输入你的年龄:'
age += '\n或者输入quit退出'
# while True:
#     ages = input(age)
#     if ages == 'quit':
#         break
#     else:
#         ages = int(ages)
#         if ages < 3:
#             print('免费')
#         elif ages >= 3 and ages <= 12:
#             print('10')
#         elif ages > 12:
#             print('15')
#         else:
#             print(ages)
# active = True
# while active:
#     ages = input(age)
#     if ages == 'quit':
#         active = False
#     else:
#         ages = int(ages)
#         if ages < 3:
#             print('免费')
#         elif ages >= 3 and ages <= 12:
#             print('10')
#         elif ages > 12:
#             print('15')
#         else:
#             print(ages)



# a = ['A','B','C','C','C','D']
# b = []
# for i in a:
#     print(i,'I like')
# while a:
#     c = a.pop()
#     print(c,'我要')
#     b.append(c)
# for i in b:
#     print(i,'已做好')
# while 'C' in a:
#     a.remove('C')
# print(a)



# a = {}
#
# active = True
# while active:
#     name = input('你叫什么名字：')
#     dream = input('你梦想的旅游胜地：')
#     a[name] = dream
#     repeat = input('还有人吗？(yes/no):')
#     if repeat == 'no':
#         active = False
# print('------------')
# for name,dream in a.items():
#     print(name,'想去',dream)


# def make_shirt(size = '大号',word = 'I love python' ):
#     print('这件T恤的尺码是',size,',字样是',word)
#
# make_shirt()
# make_shirt('中号')
# make_shirt('大大号','I ooo')

#
# def describe_city(city_name,country = 'China'):
#     print(city_name+' is in '+country)
#
# describe_city('shanghai')
# describe_city('guizhou')
# describe_city('country','usa')


# def get_name(frist_name,lastname):
#     full_name = frist_name + lastname
#     return full_name
# a = get_name('pu','xiongfei')
# print(a)

# def build_person(first_name, last_name, age=''):
#  """返回一个字典，其中包含有关一个人的信息"""
#  person = {'first': first_name, 'last': last_name}
#  if age:
#      person['age'] = age
#  return person
# musician = build_person('jimi', 'hendrix','25')
# print(musician)

# def city_country(city,country):
#     ok = '“'+ city +' '+ country + '”'
#     return ok
# c = city_country('shanghai','china')
# print(c)


# def make_album(name,album,num = ''):
#     singer = {'name':name,'album':album}
#     if num:
#         singer['num'] = num
#     return singer
# while True:
#
#      print('请输入歌手名和专辑(歌曲数可选)')
#      print('或者输入q退出')
#      p_name = input('\n请输入歌手名:')
#
#      if p_name == 'q':
#          break
#      p_singer = input('请输入专辑：')
#      if p_singer == 'q':
#          break
#      p_num = input('请输入歌曲数（可选）：')
#      if p_num == 'q':
#          break
#      name_singer = make_album(p_name, p_singer,p_num)
#      print(name_singer)

'''现在有一家厂家需要打印T恤字样'''

#这个函数将处理需要打印的和打印好的

# def get_ready_ok(ready,ok):
#     while ready:
#         a = ready.pop()
#         print('已准备打印的',a)
#         ok.append(a)
#
# def show_all(ok):
#     for mode in ok:
#         print(mode,'打印好了')
#
# l = [1,2,3,4,5]
# p = []
# get_ready_ok(l,p)
# print('-----------------------')
# show_all(p)



# magician_name = ['jaok', 'andid', 'djods', 'sddsi']
# def show_magician(magician_name):
#     for i in magician_name:
#         print(i)
# show_magician(magician_name)



# magician = ['jidai','dadda','wtye','efffa','dffej']
# def show_magicians(names):
#     for i in names:
#         print(i)
#
# show_magicians(magician)


# def show_magicians(magicians,new_magicians):
#     while magicians:
#         current_magicians = magicians.pop()
#         current_magicians = "the Great: " + current_magicians
#         new_magicians.append(current_magicians)
#
#
# def make_great(new_magicians):
#     for magician in new_magicians:
#         print(magician)
#
# magicians = ["老王", "猫猫", "登登"]
# new_magicians = []
#
# show_magicians(magicians[:],new_magicians)
#
# make_great(new_magicians)
# make_great(magicians)



# def make_pizza(size,*toppings):
#     print("\nMaking a"  + str(size) +
#           "-inch pizza with the follwing toppings:")
#     for topping in toppings:
#         print(" -" + topping)
#
# make_pizza(16,'pepperoni')
# make_pizza(12,'A','B','C')




def car_information(manufacturer,type,**arbitrarily):
    information = {}
    information['name'] = manufacturer
    information['type'] = type
    for key,value in arbitrarily.items():
        information[key] = value
    return information
a = car_information('上海一汽','小车',上海大众 ='SUV')
print(a)

