import pygame
from app_config import enemies_cnt

walk_left_img = None
walk_right_img = None
walk_up_img = None
walk_down_img = None
map_img = None
coin_img = None
win_window_img = None
loss_window_img = None
ghosts_imgs = []


def load_images():
    global walk_left_img
    global walk_right_img
    global walk_up_img
    global walk_down_img
    global map_img
    global ghosts_imgs
    global coin_img
    global win_window_img
    global loss_window_img

    walk_left_img = pygame.image.load('sprites/pacmanL.png')
    walk_right_img = pygame.image.load('sprites/pacmanR.png')
    walk_up_img = pygame.image.load('sprites/pacmanU.png')
    walk_down_img = pygame.image.load('sprites/pacmanD.png')
    map_img = pygame.image.load('sprites/map.png')
    coin_img = pygame.image.load('sprites/coin.png')
    win_window_img = pygame.image.load('sprites/win_window.png')
    loss_window_img = pygame.image.load('sprites/loss_window.png')

    for i in range(enemies_cnt):
        ghosts_imgs.append(pygame.image.load(f'sprites/ghost-{str(i)}.png'))
