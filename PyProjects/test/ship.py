import pygame


class Ship:
    """定义飞船类"""
    def __init__(self, ai_settings, screen):
        """初始化属性值，引入设置值，屏幕作为其参照系"""
        self.ai_settings = ai_settings
        self.screen = screen

        # 加载飞船图片
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        # 设置飞船与屏幕的相对关系
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)  # 为啥要转换成浮点数呢？
        
        # 设置飞船的起始状态
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """更新飞船位置"""
        if self.moving_right and self.screen_rect.right > self.rect.right:
            # 飞船向右移动
            print("右")
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.screen_rect.left < self.rect.left:
            # 飞船向左移动
            print("左")
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
