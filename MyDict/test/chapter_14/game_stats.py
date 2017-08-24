class GameStats():
    """Track statistics for Alien Invasion."""
    # ## 外星人入侵的跟踪统计。
    
    def __init__(self, ai_settings):
        """Initialize statistics."""
        # ## 初始化数据。
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # Start game in an inactive state.
        # ## 开始游戏的活性。
        self.game_active = False
        
        # High score should never be reset.
        # ## 高分不能重置。
        self.high_score = 0
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        # ## 初始化统计数据可以在游戏中改变。
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
