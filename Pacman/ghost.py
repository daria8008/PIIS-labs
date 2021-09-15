from agent import *
import random
import images
import map

class Ghost(Agent):
    id = None

    def __init__(self, id, x, y):
        super(Ghost, self).__init__(x, y)
        self.id = id
        self.change_direction()

    def change_direction(self):
        dir = random.choice(["left", "right", "up", "down"])

        if dir == "left":
            self.is_walking_left = True
            self.is_walking_right = False
            self.is_walking_up = False
            self.is_walking_down = False
        if dir == "right":
            self.is_walking_left = False
            self.is_walking_right = True
            self.is_walking_up = False
            self.is_walking_down = False
        if dir == "up":
            self.is_walking_left = False
            self.is_walking_right = False
            self.is_walking_up = True
            self.is_walking_down = False
        if dir == "down":
            self.is_walking_left = False
            self.is_walking_right = False
            self.is_walking_up = False
            self.is_walking_down = True

    def walk(self, speed):
        if self.is_walking_left:
            if map.is_wall(self.x - 1, self.y):
                self.change_direction()
                self.walk(speed)
            else:
                self.x -= speed
        elif self.is_walking_right:
            if map.is_wall(self.x + 1, self.y):
                self.change_direction()
                self.walk(speed)
            else:
                self.x += speed
        elif self.is_walking_down:
            if map.is_wall(self.x, self.y + 1):
                self.change_direction()
                self.walk(speed)
            else:
                self.y += speed
        elif self.is_walking_up:
            if map.is_wall(self.x, self.y - 1):
                self.change_direction()
                self.walk(speed)
            else:
                self.y -= speed


    def get_image(self):
        return images.ghosts_imgs[self.id]
