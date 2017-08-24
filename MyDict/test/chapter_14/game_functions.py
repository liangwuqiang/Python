import sys
from time import sleep

import pygame

from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    # ## 响应按键。
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
        
def check_keyup_events(event, ship):
    """Respond to key releases."""
    # ## 应对关键版本。
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens,
        bullets):
    """Respond to keypresses and mouse events."""
    # ## 响应按键和鼠标事件。
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button,
                ship, aliens, bullets, mouse_x, mouse_y)
            
def check_play_button(ai_settings, screen, stats, sb, play_button, ship,
        aliens, bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    # ## 当玩家点击开始一个新的游戏。
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        # ## 重置游戏设置。
        ai_settings.initialize_dynamic_settings()
        
        # Hide the mouse cursor.
        # ## 隐藏鼠标光标。
        pygame.mouse.set_visible(False)
        
        # Reset the game statistics.
        # ## 重置游戏统计数据。
        stats.reset_stats()
        stats.game_active = True
        
        # Reset the scoreboard images.
        # ## 重置记分板图片。
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        
        # Empty the list of aliens and bullets.
        # ## 空的外星人和子弹的列表。
        aliens.empty()
        bullets.empty()
        
        # Create a new fleet and center the ship.
        # ## 创建一个新的船舰队和中心。
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet, if limit not reached yet."""
    # ## 火一颗子弹,如果没有达到极限。
    # Create a new bullet, add to bullets group.
    # ## 创建一个新的子弹,子弹群。
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
        play_button):
    """Update images on the screen, and flip to the new screen."""
    # ## 更新图像在屏幕上,翻转到新屏幕。
    # Redraw the screen, each pass through the loop.
    # ## 屏幕重绘,每个通过循环。
    screen.fill(ai_settings.bg_color)
    
    # Redraw all bullets, behind ship and aliens.
    # ## 重画所有的子弹,在船和外星人。
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    
    # Draw the score information.
    # ## 画出得分信息。
    sb.show_score()
    
    # Draw the play button if the game is inactive.
    # ## 画出播放按钮,如果游戏活动。
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    # ## 使最近绘制屏幕可见。
    pygame.display.flip()
    
def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Update position of bullets, and get rid of old bullets."""
    # ## 更新子弹的位置,摆脱旧的子弹。
    # Update bullet positions.
    # ## 更新子弹的位置。
    bullets.update()

    # Get rid of bullets that have disappeared.
    # ## 摆脱已经消失的子弹。
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship,
        aliens, bullets)
        
def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    # ## 检查是否有新的高分。
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
            
def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship,
        aliens, bullets):
    """Respond to bullet-alien collisions."""
    # ## 应对bullet-alien碰撞。
    # Remove any bullets and aliens that have collided.
    # ## 删除任何子弹和外星人相撞。
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    
    if len(aliens) == 0:
        # If the entire fleet is destroyed, start a new level.
        # ## 如果整个舰队摧毁,开始一个新的水平。
        bullets.empty()
        ai_settings.increase_speed()
        
        # Increase level.
        # ## 提高水平。
        stats.level += 1
        sb.prep_level()
        
        create_fleet(ai_settings, screen, ship, aliens)
    
def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    # ## 如果任何外星人已经达到优势做出适当的回应。
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
        
def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet, and change the fleet's direction."""
    # ## 降低整个舰队,舰队的方向改变。
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
    
def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Respond to ship being hit by alien."""
    # ## 应对船舶被外星人袭击。
    if stats.ships_left > 0:
        # Decrement ships_left.
        # ## 减量ships_left。
        stats.ships_left -= 1
        
        # Update scoreboard.
        # ## 更新记分牌。
        sb.prep_ships()
        
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    
    # Empty the list of aliens and bullets.
    # ## 空的外星人和子弹的列表。
    aliens.empty()
    bullets.empty()
    
    # Create a new fleet, and center the ship.
    # ## 创建一个新的车队,船中心。
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()
    
    # Pause.
    # ## 休息。
    sleep(0.5)
    
def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens,
        bullets):
    """Check if any aliens have reached the bottom of the screen."""
    # ## 检查是否有外星人到达底部的屏幕上。
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            # ## 如果船上有治疗这种一样的打击。
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break
            
def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """
    Check if the fleet is at an edge,
    # ## 检查是否在一个舰队,
      then update the postions of all aliens in the fleet.
      # ## 然后更新岗位的外星人舰队。
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    
    # Look for alien-ship collisions.
    # ## 寻找外星船只碰撞。
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)

    # Look for aliens hitting the bottom of the screen.
    # ## 寻找外星人触及屏幕底部的。
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)
            
def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    # ## 确定合适的外国人数量。
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
    
def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    # ## 确定外星人的行数,适合在屏幕上。
    available_space_y = (ai_settings.screen_height -
                            (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
    
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien, and place it in the row."""
    # ## 创建一个外星人,并把它的行。
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens."""
    # ## 创建一个完整的外星人。
    # Create an alien, and find number of aliens in a row.
    # ## 创建一个外星人,发现外星人在一行的数量。
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
        alien.rect.height)
    
    # Create the fleet of aliens.
    # ## 创建的外星人。
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,
                row_number)
