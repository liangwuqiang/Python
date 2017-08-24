import sys

import pygame
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    # ## 响应按键。
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group.
        # ## 创建一个新的子弹,并将它添加到子弹。
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        
def check_keyup_events(event, ship):
    """Respond to key releases."""
    # ## 应对关键版本。
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
        
def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    # ## 响应按键和鼠标事件。
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen."""
    # ## 更新图像在屏幕上和翻转到新屏幕。
    # Redraw the screen during each pass through the loop.
    # ## 屏幕重绘在每个通过循环。
    screen.fill(ai_settings.bg_color)
    
    # Redraw all bullets behind ship and aliens.
    # ## 重画所有子弹船和外星人。
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # Make the most recently drawn screen visible.
    # ## 使最近绘制屏幕可见。
    pygame.display.flip()
