from random import choice

class RandomWalk():
    """A class to generate random walks."""
    # ## 一个类来生成随机漫步。
    
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        # ## 初始化属性的行走。
        self.num_points = num_points
        
        # All walks start at (0, 0).
        # ## 各行各业开始(0,0)。
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""
        # ## 计算所有的点在走。
        
        # Keep taking steps until the walk reaches the desired length.
        # ## 继续采取措施,直到走到所需长度。
        while len(self.x_values) < self.num_points:
            
            # Decide which direction to go, and how far to go in that direction.
            # ## 决定去哪个方向,朝这个方向走多远。
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            
            # Reject moves that go nowhere.
            # ## 拒绝行动,无处可去。
            if x_step == 0 and y_step == 0:
                continue
            
            # Calculate the next x and y values.
            # ## 计算下一个x和y值。
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)
    
