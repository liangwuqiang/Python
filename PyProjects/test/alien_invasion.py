import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    print('游戏开始') 
    pygame.init()   # 游戏初始化
    ai_settings = Settings()    # 取得游戏设置
    
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))   # 设置游戏模式
    pygame.display.set_caption('外星人入侵')     # 设置窗口标题名称
    
    ship = Ship(ai_settings, screen)   # 创建飞船

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()
