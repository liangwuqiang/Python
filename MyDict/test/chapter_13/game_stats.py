class GameStats():
    """Track statistics for Alien Invasion."""
    # ## 外星人入侵的跟踪统计。
    
    def __init__(self, ai_settings):
        """Initialize statistics."""
        # ## 初始化数据。
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # Start Alien Invasion in an active state.
        # ## 开始在一个活跃的外星人入侵的状态。
        self.game_active = True
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        # ## 初始化统计数据可以在游戏中改变。
        self.ships_left = self.ai_settings.ship_limit
