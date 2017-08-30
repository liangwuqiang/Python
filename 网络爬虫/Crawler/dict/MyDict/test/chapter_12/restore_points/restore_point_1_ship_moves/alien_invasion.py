import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # ## Initialize the pygame, Settings, and the screen object.
    # ## Pygame initialization
    # ## Instantiated set up the class
    # ## Get the screen parameters
        (ai_settings.screen_width, ai_settings.screen_height))
    # ## Set the title
    
    # ## Set the background color
    bg_color = (230, 230, 230)
    
    # ## Create a spaceship
    ship = Ship(ai_settings, screen)
    
    # ## Start the game loop
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
        
run_game()
