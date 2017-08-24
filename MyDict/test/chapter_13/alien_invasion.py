import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
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
    
    # Create an instance to store game statistics.
    # ## 创建一个实例存储游戏数据。
    stats = GameStats(ai_settings)
    
    # Set the background color.
    # ## 设置背景颜色。
    bg_color = (230, 230, 230)
    
    # Make a ship, a group of bullets, and a group of aliens.
    # ## 一艘船,一群子弹,和一群外星人。
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    # Create the fleet of aliens.
    # ## 创建的外星人。
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    # ## 开始为游戏主循环。
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
