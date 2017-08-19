import pygame


class Ship:
    """定义飞船类"""
    def __init__(self, ai_settings, screen):
        """初始化飞船，并设置它的开始位置"""
        self.ai_settings = ai_settings
        self.screen = screen

        # 加载飞船图片，并取得它的四边形
        self.image = pygame.image.load('images/ship')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 启动每个新飞船在屏幕底部中间
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 储存飞船中心的值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """更新飞船位置，基于移动标志"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blime(self):
        """在当前位置画飞船"""
        self.screen.blit(self.image, self.rect)

