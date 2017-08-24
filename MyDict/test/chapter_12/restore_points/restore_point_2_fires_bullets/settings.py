class Settings():
    """A class to store all settings for Alien Invasion."""
    # ## 外星人入侵的一个类来存储所有设置。
    def __init__(self):
        """Initialize the game's settings."""
        # ## 初始化游戏的设置。
        # Screen settings
        # ## 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # Ship settings
        # ## 船设置
        self.ship_speed_factor = 1.5

        # Bullet settings
        # ## 子弹的设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
