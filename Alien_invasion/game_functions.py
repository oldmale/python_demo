#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 17:12
# @Author  : Puxf
# @Site    : 
# @File    : game_functions.py
# @Software: PyCharm


import sys
import pygame

def check_events(ship):
    """响应按键和鼠标"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left =False

def update_screen(ai_settings,scren,ship):
    """更新屏幕上的图像，并切换新屏幕"""
    #每次循环时都重绘屏幕
    scren.fill(ai_settings.bg_color)
    ship.blitme()

    #让最近绘制的屏幕可见
    pygame.display.flip()


