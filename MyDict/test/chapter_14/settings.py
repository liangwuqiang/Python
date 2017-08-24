class Settings():
    """A class to store all settings for Alien Invasion."""
    # ## 外星人入侵的一个类来存储所有设置。

    def __init__(self):
        """Initialize the game's static settings."""
        # ## 初始化游戏的静态设置。
        # Screen settings.
        # ## 屏幕上设置。
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # Ship settings.
        # ## 船设置。
        self.ship_limit = 3
            
        # Bullet settings.
        # ## 子弹的设置。
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
        # Alien settings.
        # ## 外星人的设置。
        self.fleet_drop_speed = 10
            
        # How quickly the game speeds up.
        # ## 游戏加速的速度有多快。
        self.speedup_scale = 1.1
        # How quickly the alien point values increase.
        # ## 外星人点值的速度增加。
        self.score_scale = 1.5
    
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        # ## 初始化设置改变整个游戏。
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        
        # Scoring.
        # ## 得分。
        self.alien_points = 50
    
        # fleet_direction of 1 represents right, -1 represents left.
        # ## 
        self.fleet_direction = 1
        
    def increase_speed(self):
        """Increase speed settings and alien point values."""
        # ## 提高速度设置和外星人点值。
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
