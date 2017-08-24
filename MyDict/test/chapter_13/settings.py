class Settings():
    """A class to store all settings for Alien Invasion."""
    # ## 外星人入侵的一个类来存储所有设置。

    def __init__(self):
        """Initialize the game's settings."""
        # ## 初始化游戏的设置。
        # Screen settings.
        # ## 屏幕上设置。
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings.
        # ## 船设置。
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Bullet settings.
        # ## 子弹的设置。
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
        # Alien settings.
        # ## 外星人的设置。
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right, -1 represents left.
        # ## fleet_direction 1代表正确,1代表了。
        self.fleet_direction = 1
