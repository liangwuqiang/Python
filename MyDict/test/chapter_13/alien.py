import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    # ## 一个类代表一个外星舰队中。

    def __init__(self, ai_settings, screen):
        """Initialize the alien, and set its starting position."""
        # ## 初始化外星人,并设置其起始位置。
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image, and set its rect attribute.
        # ## 
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        # ## 开始每一个新的外星人在屏幕的左上角。
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        # ## 存储外星人的确切位置。
        self.x = float(self.rect.x)
        
    def check_edges(self):
        """Return True if alien is at edge of screen."""
        # ## 返回True,如果外星人是在屏幕的边缘。
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
    def update(self):
        """Move the alien right or left."""
        # ## 外星人的左右移动。
        self.x += (self.ai_settings.alien_speed_factor *
                        self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """Draw the alien at its current location."""
        # ## 画出外星人在其当前位置。
        self.screen.blit(self.image, self.rect)
