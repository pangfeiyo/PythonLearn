# 13-1  星星 ：找一幅星星图像，并在屏幕上显示一系列整齐排列的星星。
import pygame
import sys
from pygame.sprite import Group
from pygame.sprite import Sprite


class Start(Sprite):
    """docstring for Start"""

    def __init__(self, screen):
        super(Start, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('12-2.jpg')
        self.rect = self.image.get_rect()

        # 设置位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    bg_color = (255,255,255)
    pygame.display.set_caption("all start")
    start = Group()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        create_start(start,screen)
        screen.fill(bg_color)
        start.draw(screen)
        pygame.display.flip()


def create_start(start,screen):
    start1 = Start(screen)
    start_width = start1.rect.width
    avaliable_x = 1200 - 2*start_width
    number_x = int(avaliable_x / (2 * start_width))
    start_height = start1.rect.height
    avaliable_y = 800 - 2* start_height
    number_y = int (avaliable_y / (2 * start_height))
    for n_y in range(number_y):
        for n_x in range(number_x):
            st = Start(screen)
            st.x = start_width + 2 * start_width * n_x
            st.y = start_height + 2 * start_height * n_y
            st.rect.x = st.x
            st.rect.y = st.y
            start.add(st)


run_game()