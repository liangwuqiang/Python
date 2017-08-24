from random import randint

class Die():
    """A class representing a single die."""
    # ## 一个类代表一个死。
    
    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        # ## 假设一个六面骰子。
        self.num_sides = num_sides
        
    def roll(self):
        """"Return a random value between 1 and number of sides."""
        # ## “返回一个随机的值介于1和许多。
        return randint(1, self.num_sides)
