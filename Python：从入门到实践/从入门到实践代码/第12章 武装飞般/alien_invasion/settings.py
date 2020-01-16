# 模块
# 存放设置

class Settings():
    '''存储《外星人入侵》的所有设置的类'''

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕（screen）设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # 飞船的设置
        # 这个属性决定飞船在每次循环时最多移动多少距离，现在每次移动1.5像素而不是1像素
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 3    # 子弹速度
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3    # 限制子弹数量

        # 外星人设置
        self.alien_speed_factor = 1 # 移动速度
        self.fleet_drop_speed = 10  # 向下移动的速度
        # fleet_direction 为1表示向右，为-1表示向左
        self.fleet_direction = 1
