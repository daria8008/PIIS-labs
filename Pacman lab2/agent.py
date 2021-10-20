class Agent:
    x = 0
    y = 0
    is_walking_left = False
    is_walking_right = False
    is_walking_up = False
    is_walking_down = False

    def __init__(self, x, y):
        self.x = x
        self.y = y
