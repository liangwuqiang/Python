import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""
    # ## 一个类来管理从船上子弹。

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object, at the ship's current position."""
        # ## 创建一个子弹对象,在船的当前位置。
        super(Bullet, self).__init__()
        self.screen = screen

        # Create bullet rect at (0, 0), then set correct position.
        # ## 创建子弹矩形在(0,0),然后设置正确的位置。
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # Store a decimal value for the bullet's position.
        # ## 存储一个十进制值子弹的位置。
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        # ## 子弹的屏幕上移动。
        # Update the decimal position of the bullet.
        # ## 子弹的小数点位置更新。
        self.y -= self.speed_factor
        # Update the rect position.
        # ## 矩形的位置更新。
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        # ## 画出子弹到屏幕上。
        pygame.draw.rect(self.screen, self.color, self.rect)
