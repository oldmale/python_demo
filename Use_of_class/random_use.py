#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/27 16:52
# @Author  : Puxf
# @Site    : 
# @File    : random.py
# @Software: PyCharm

import random

"""9-14 骰子：模块 random 包含以各种方式生成随机数的函数，其中的 randint()返回
一个位于指定范围内的整数，例如，下面的代码返回一个 1~6 内的整数：
from random import randint
x = randint(1, 6)
请创建一个 Die 类，它包含一个名为 sides 的属性，该属性的默认值为 6。编写一
个名为 roll_die()的方法，它打印位于 1 和骰子面数之间的随机数。创建一个 6 面的骰
子，再掷 10 次。
创建一个 10 面的骰子和一个 20 面的骰子，并将它们都掷 10 次。"""

class Die():
    """骰子"""

    def __init__(self,sides=6):
        """初始化属性设默认值"""
        self.sides = sides

    def roll_die(self):
        """打印位于 1 和骰子面数之间的随机数"""
        return random.randint(1,self.sides)


die = Die(10)
s = []
for i in range(20):
    i = die.roll_die()
    s.append(i)
print(s)






