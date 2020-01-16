# 12-1  蓝色天空 ：创建一个背景为蓝色的 Pygame 窗口。
import pygame
import sys



'''屏幕设置'''
width = 1344
height = 768
bg_color = (0,0,255)

def run_game():
    '''主程序'''
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    # 初始化一个窗口或屏幕进行显示
    s = pygame.display.set_mode(
        (width, height))

    # 需要一个循环来重新绘制这个窗口，不然会闪一下就消失了
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        s.fill(bg_color)
        pygame.display.flip()


run_game()