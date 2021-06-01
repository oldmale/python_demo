#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 10:22
# @Author  : Puxf
# @Site    : 
# @File    : city_functions.py.py
# @Software: PyCharm

def get_city_state(city,state,population=''):
    """返回城市和国家的函数"""
    if population:
        full_city_state = city + ',' + state + ' - ' + population
    else:
        full_city_state = city + ',' + state
    return full_city_state.title()

# a = get_city_state('shanjn','chaili')
# print(a)