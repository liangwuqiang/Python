import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()   # 游戏初始化
    ai_settings = Settings()    # 取得设置值
    screen = pygame.display.set_mode(   # 返回游戏屏幕
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption('外星人入侵') # 设置游戏标题

    ship = Ship(ai_settings, screen)    # 取得飞船的实例

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()
