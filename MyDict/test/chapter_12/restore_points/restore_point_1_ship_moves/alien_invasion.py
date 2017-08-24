import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化 pygame, settings, 和 screen 对象.
    # ## Initialize the pygame, Settings, and the screen object.
    pygame.init()   # pygame 初始化
    # ## Pygame initialization
    ai_settings = Settings()    # 实例化设置类
    # ## Instantiated set up the class
    screen = pygame.display.set_mode(   # 取得屏幕参数
    # ## Get the screen parameters
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("外星人入侵")     # 设置标题
    # ## Set the title
    
    # 设置背景色
    # ## Set the background color
    bg_color = (230, 230, 230)
    
    # 创建飞船
    # ## Create a spaceship
    ship = Ship(ai_settings, screen)
    
    # 启动游戏循环
    # ## Start the game loop
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
        
run_game()
