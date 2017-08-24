import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and screen object.
    # ## pygame进行初始化,设置,和屏幕对象。
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Set the background color.
    # ## 设置背景颜色。
    bg_color = (230, 230, 230)
    
    # Make a ship.
    # ## 一艘船。
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    # ## 让子弹存储在一组。
    bullets = Group()
    
    # Start the main loop for the game.
    # ## 开始为游戏主循环。
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)
        
run_game()
