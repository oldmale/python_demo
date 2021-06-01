#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 13:26
# @Author  : Puxf
# @Site    : 
# @File    : alien_invasion.py
# @Software: PyCharm
import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_heigth))
    pygame.display.set_caption("Alien Invasion")

    bg_color = (ai_settings.bg_color)
    ship = Ship(screen)
    # 开始游戏的主循环
    while True:
        gf.check_events(ship)
        ship.update()
        # # 监视键盘和鼠标事件
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        # #每次循环时都重绘屏幕
        # screen.fill(bg_color)
        # ship.blitme()
        # # 让最近绘制的屏幕可见
        # pygame.display.flip()
        gf.update_screen(ai_settings,screen,ship)

run_game()



