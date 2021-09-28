import pygame
from agent import *
import images
import map
import state


class Pacman(Agent):
    def walk(self, speed):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and not map.is_wall(self.x - 1, self.y):
            self.x -= speed
            self.is_walking_left = True
            self.is_walking_right = False
            self.is_walking_up = False
            self.is_walking_down = False
        if keys[pygame.K_RIGHT] and not map.is_wall(self.x + 1, self.y):
            self.x += speed
            self.is_walking_left = False
            self.is_walking_right = True
            self.is_walking_up = False
            self.is_walking_down = False
        if keys[pygame.K_DOWN] and not map.is_wall(self.x, self.y + 1):
            self.y += speed
            self.is_walking_left = False
            self.is_walking_right = False
            self.is_walking_up = False
            self.is_walking_down = True
        if keys[pygame.K_UP] and not map.is_wall(self.x, self.y - 1):
            self.y -= speed
            self.is_walking_left = False
            self.is_walking_right = False
            self.is_walking_up = True
            self.is_walking_down = False

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
