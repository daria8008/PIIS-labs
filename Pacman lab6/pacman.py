from agent import *
import images
import map
import state_file
import dqn_step_action
from common import Position


class Pacman(Agent):

    def walk(self, action_item):
        # next_position = minimax.minimax(Position(self.x, self.y), ghosts)
        next_position = dqn_step_action.dqn_pacman_action(Position(self.x, self.y), action_item)
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
        if map.coins_map.map[self.y][self.x]:
            map.coins_map.map[self.y][self.x] = False
            state_file.score += 1
