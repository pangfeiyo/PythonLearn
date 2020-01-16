'''创建pygame窗口以及响应用户输入'''
# 主程序不需要导入 sys 模块的原因是：在模块 game_functions.py 中使用了它
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button



def run_game():
    # 初始化游戏并创建一个屏幕对象
    # （新增settings.py后，初始化pygame、设置和屏幕对象）
    pygame.init()

    # 创建屏幕
    ai_settings = Settings()
    # display 设置重叠像素数据     set.mode 初始化一个窗口或屏幕进行显示
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件(event)
        gf.check_events(ai_settings, screen, stats, play_button, ship,
                      aliens, bullets)

        # 如果状态为True
        if stats.game_active:
        
            # 每次执行循环时都调用飞船的方法 update()
            ship.update()

            # 更新子弹编组
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)

            # 更新外星人位置
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        #更新屏幕上的图像，并切换到屏幕
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets,
                         play_button)

run_game()