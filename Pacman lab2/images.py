import pygame

walk_left_img = None
walk_right_img = None
walk_up_img = None
walk_down_img = None
map_img = None
coin_img = None


def load_images():
    global walk_left_img
    global walk_right_img
    global walk_up_img
    global walk_down_img
    global map_img
    global coin_img

    walk_left_img = pygame.image.load('sprites/pacmanL.png')
    walk_right_img = pygame.image.load('sprites/pacmanR.png')
    walk_up_img = pygame.image.load('sprites/pacmanU.png')
    walk_down_img = pygame.image.load('sprites/pacmanD.png')
    map_img = pygame.image.load('sprites/map.png')
    coin_img = pygame.image.load('sprites/coin.png')