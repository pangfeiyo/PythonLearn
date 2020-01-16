# ship 船 模块
import pygame

class Ship():

    def __init__(self, ai_settings, screen):      # screen 屏幕   setting 设置
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载 ship（飞船）图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')   #load（加载、负载）  这个函数返回一个表示飞船的surface（表面），而我们将这个存到self.image中
        self.rect = self.image.get_rect()   # 获取相应的surface的属性rect（矩形）     get_rect()返回渲染文本的大小和偏移量
        # 加载 screen（屏幕）的矩形
        self.screen_rect = screen.get_rect()    # 把屏幕的矩形存储在self.screen_rect中

        # 将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx    # self.rect.centerx（飞船中心的 x坐标）设置为表示屏幕的矩形的属性centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性 center 中存储小数值
        self.center = float(self.rect.centerx)
        self.bottom = self.rect.centery

        # 移动标示
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的 center 值，而不是 rect
        # moving_right 为 True 的话，并且rect（飞船）的右值 < 屏幕的右边界
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # 飞船向右移动
            self.center += self.ai_settings.ship_speed_factor

        # moving_left 为 True 的话，并且 rect（飞船）的左边界 > 0
        if self.moving_left and self.rect.left > 0:   # moving_left 为 True 的话
            # 飞船向左移动
            self.center -= self.ai_settings.ship_speed_factor

        if self.moving_top and self.rect.top > 0:
            self.bottom -= self.ai_settings.ship_speed_factor

        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_settings.ship_speed_factor



        # 根据 self.center 更新 rect 对象
        self.rect.centerx = self.center
        self.rect.centery = self.bottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx  # 案例原句
