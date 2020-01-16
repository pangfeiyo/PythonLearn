# 12-2  游戏角色 ：找一幅你喜欢的游戏角色位图图像或将一幅图像转换为位图。
# 创建一个类，将该角色绘制到屏幕中央，并将该图像的背景色设置为屏幕背景色，
# 或将屏幕背景色设置为该图像的背景色。

import pygame
import sys

class Ship():
    def __init__(self,screen):
        '''初始化飞船并设置其初始位置'''
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('12-2.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.center = self.screen_rect.center

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)

def run_game():
    '''初始化游戏并创建一个屏幕对象'''
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("12-2")

    bg_color = (230,230,5)

    # 创建一艘新飞船
    ship = Ship(screen)

    # 开始游戏循环
    while True:
        #监视鼠标和键盘事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环时都重绘屏幕
        #添加背景颜色
        screen.fill(bg_color)
        ship.blitme()

        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()

