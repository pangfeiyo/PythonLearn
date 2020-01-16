# 12-4  按键 ：创建一个程序，显示一个空屏幕。
# 在事件循环中，每当检测到 pygame.KEYDOWN 事件时都打印属性 event.key 。
# 运行这个程序，并按各种键，看看Pygame 如何响应。

import sys
import pygame

def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()

    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("12-4 按键")
    bg_color = (230,215,47)

    # 开始游戏主循环
    while True:

        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                        print(event.key)
                        '''
                        内容出自CSDN
                        您这个12-4是跟着自己的感觉走的吧，原题让打印属性 event.key，您这个都改成自己的颜色了。
                        想知道原题的效果，我自己弄出来的是没有任何改变，不过cmd命令行会打印很多数字，应该是按键一一对应的数字吧？
                        '''



        screen.fill(bg_color)

        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()



