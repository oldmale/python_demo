#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 15:11
# @Author  : Puxf
# @Site    : 
# @File    : settings.py
# @Software: PyCharm


class Settings():
    """储存游戏的所有设置类"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1000
        self.screen_heigth = 600
        self.bg_color = (230,230,230)

        #飞船的速度
        self.ship_speed_factor = 1.5

