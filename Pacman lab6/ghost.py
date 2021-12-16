from agent import *
import path_finder_by_bfs
import expectimax
from common import Position
from app_config import speed
import images
import map
import random
import numpy as np


class Ghost(Agent):
    id = None

    def __init__(self, id, x, y, previous_x, previous_y):
        super(Ghost, self).__init__(x, y)
        self.previous_x = previous_x
        self.previous_y = previous_y
        self.id = id
        self.change_direction()

    def change_direction(self):
        direction = random.choice(["left", "right", "up", "down"])

        if direction == "left":
            self.is_walking_left = True
            self.is_walking_right = False
            self.is_walking_up = False
            self.is_walking_down = False
        if direction == "right":
            self.is_walking_left = False
            self.is_walking_right = True
            self.is_walking_up = False
            self.is_walking_down = False
        if direction == "up":
            self.is_walking_left = False
            self.is_walking_right = False
            self.is_walking_up = True
            self.is_walking_down = False
        if direction == "down":
            self.is_walking_left = False
            self.is_walking_right = False
            self.is_walking_up = False
            self.is_walking_down = True

    def _walk_random(self):
        if self.is_walking_left:
            if map.is_wall(self.x - 1, self.y):
                self.change_direction()
                self._walk_random()
            else:
                self.x -= speed
        elif self.is_walking_right:
            if map.is_wall(self.x + 1, self.y):
                self.change_direction()
                self._walk_random()
            else:
                self.x += speed
        elif self.is_walking_down:
            if map.is_wall(self.x, self.y + 1):
                self.change_direction()
                self._walk_random()
            else:
                self.y += speed
        elif self.is_walking_up:
            if map.is_wall(self.x, self.y - 1):
                self.change_direction()
                self._walk_random()
            else:
                self.y -= speed

    def walk_optimal(self, pacman_pos):
        type_of_walk = np.random.choice([1, 2], 1, p=[0.3, 0.7])
        if type_of_walk == 1:
            self._walk_random()
        else:
            next_position = path_finder_by_bfs.find_path_by_bfs(Position(self.x, self.y), pacman_pos)

            self.x = next_position.x
            self.y = next_position.y

    def walk_random(self, pacman_pos):
        next_position = expectimax.expectimax(Position(self.x, self.y),
                                              Position(self.previous_x, self.previous_y), pacman_pos)

        self.previous_x = self.x
        self.previous_y = self.y

        self.x = next_position.x
        self.y = next_position.y

    def get_image(self):
        return images.ghosts_imgs[self.id]
