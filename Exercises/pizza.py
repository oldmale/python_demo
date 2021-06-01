#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/26 13:25
# @Author  : Puxf
# @Site    : 
# @File    : pizza.py
# @Software: PyCharm


def make_pizza(size,*toppings):
    print('\nMakeing a'+ str(size)+
          '-inch pizza with the following toppings:')
    for topping in toppings:
        print(topping)
