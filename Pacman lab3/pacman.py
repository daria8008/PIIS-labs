from agent import *
import images
import map
import state
import minimax
from common import Position


class Pacman(Agent):

    def walk(self, ghosts):
        next_position = minimax.minimax(Position(self.x, self.y), ghosts)

        self.x = next_position.x
        self.y = next_position.y

    def get_image(self):
        if self.is_walking_left:
            return images.walk_left_img
        elif self.is_walking_right:
            return images.walk_right_img
        elif self.is_walking_up:
            return images.walk_up_img
        elif self.is_walking_down:
            return images.walk_down_img
        else:
            return images.walk_right_img

    def eat_coins(self):
        if map.coins_map[self.y][self.x]:
            map.coins_map[self.y][self.x] = False
            state.score += 1
