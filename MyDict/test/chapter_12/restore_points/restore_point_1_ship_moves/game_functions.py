import sys

import pygame


def check_keydown_events(event, ship):
    """响应按键按下"""
    # ## Response to a button press
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
        

def check_keyup_events(event, ship):
    """响应按键弹起"""
    # ## The response button pop-up
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    """响应按键和鼠标事件"""
    # ## Response keys and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    """更新屏幕图像，弹到新屏幕"""
    # ## Update the screen image, play to the new screen
    # 重画屏幕，在每次过场循环中
    # ## Redraw the screen every time cut cycle
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # 使最近回执的屏幕可见
    # ## Recent receipt screen is visible
    pygame.display.flip()
