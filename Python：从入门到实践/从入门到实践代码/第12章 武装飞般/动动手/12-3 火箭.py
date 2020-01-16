# 编写一个游戏，开始时屏幕中央有一个火箭，
# 而玩家可使用四个方向键上下左右移动火箭。
# 请务必确保火箭不会移到屏幕外面。

import sys
import pygame

class Ship:
    '''初始化图片并设置其初始位置'''
    def __init__(self,ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('12-2.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.center = self.screen_rect.center

        # 创建飞船属性 center
        self.center = self.rect.centerx
        self.bottom = self.rect.centery

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def update(self):
        '''根据移动标志调整飞船位置'''
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right <self.screen_rect.right:
            self.center += 1
        if self.moving_left and self.rect.left > 0:
            self.center -= 1
        if self.moving_top and self.rect.top > 0:
            self.bottom -=1
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += 1

        # 根据self.center 更新 rect 对象是
        self.rect.centerx = self.center
        self.rect.centery = self.bottom

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)

def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # 向右移动飞船
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                # 向左移动飞船
                ship.moving_left = True
            elif event.key == pygame.K_UP:
                # 向上移动飞船
                ship.moving_top = True
            elif event.key == pygame.K_DOWN:
                # 向下移动飞船
                ship.moving_bottom = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
            elif event.key == pygame.K_UP:
                ship.moving_top = False
            elif event.key == pygame.K_DOWN:
                ship.moving_bottom = False


def update_screen(ai_settings, ship, screen):
    '''更新屏幕上的图像，并切换到新屏幕'''
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 飞船位置
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()


class Setting():
    '''存储所有设置的类'''

    def __init__(self):
        '''初始化游戏的设置'''
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (148,98,145)


def run_game():
    '''初始化游戏并创建一个屏幕对象'''
    pygame.init()

    ai_settings = Setting()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("12-3 火箭")

    ship = Ship(ai_settings, screen)

    # 开始游戏循环
    while True:
        # 监视鼠标和键盘事件
        check_events(ship)

        # 每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.update()

        update_screen(ai_settings, ship, screen)

run_game()