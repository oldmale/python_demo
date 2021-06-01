#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 15:23
# @Author  : Puxf
# @Site    : 
# @File    : ship.py
# @Software: PyCharm


import pygame

class Ship():

    def __init__(self,ai_settings,screen):
        """初始化飞船并设置初始位置"""
        self.screen = screen
        self.settings = ai_settings

        #获取飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)
