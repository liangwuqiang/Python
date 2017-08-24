class Settings():
    """一个类用来存储《外星人入侵》的设置"""
    # ## A class used to store the alien invasion

    def __init__(self):
        """初始化游戏设置"""
        # ## Initialize the game Settings
        # 屏幕设置
        # ## Set up the screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        # ## Ship set
        self.ship_speed_factor = 1.5

        # 子弹设置
        # ## The bullet set
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
