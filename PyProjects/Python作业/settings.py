class Settings:
    """用于保存《外星人入侵》游戏的所有设置的一个类"""
    def __init__(self):
        """初始化游戏设置"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed_factor = 1.5
