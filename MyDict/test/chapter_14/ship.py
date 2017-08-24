import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """Initialize the ship, and set its starting position."""
        # ## 初始化,并设置其起始位置。
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image, and get its rect.
        # ## 负载船形象,和矩形。
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        # ## 开始每个新船屏幕底部的中心。
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # Store a decimal value for the ship's center.
        # ## 为船舶中心存储一个十进制值。
        self.center = float(self.rect.centerx)
        
        # Movement flags.
        # ## 运动的旗帜。
        self.moving_right = False
        self.moving_left = False
        
    def center_ship(self):
        """Center the ship on the screen."""
        # ## 中心屏幕上的船。
        self.center = self.screen_rect.centerx
        
    def update(self):
        """Update the ship's position, based on movement flags."""
        # ## 更新船的位置,基于运动的旗帜。
        # Update the ship's center value, not the rect.
        # ## 更新船的中心价值,而不是矩形。
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            
        # Update rect object from self.center.
        # ## 更新从self.center矩形对象。
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        # ## 画船在它的当前位置。
        self.screen.blit(self.image, self.rect)
