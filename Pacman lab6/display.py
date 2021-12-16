import pygame
import images
from app_config import *
import state_file
window = None


def init():
    global window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Pacman")


def draw_window():
    global window
    window.blit(images.map_img, (0, 0))


def draw_agent(agent):
    global window
    window.blit(agent.get_image(), (agent.x * cell_size, agent.y * cell_size))


def draw_coins(positions):
    global window
    for pos in positions:
        window.blit(images.coin_img, (pos.x * cell_size, pos.y * cell_size))


def update_screen():
    pygame.display.update()


def display_score():
    pygame.font.init()

    myfont = pygame.font.SysFont('Comic Sans MS', 26)
    textsurface = myfont.render(f'Score: {state_file.score}', False, YELLOW)
    window.blit(textsurface, (SCORE_POS_X, SCORE_POS_Y))


def display_win_window():
    window = pygame.display.set_mode((WIN_WINDOW_WIDTH, WIN_WINDOW_HEIGHT))
    window.blit(images.win_window_img, (0, 0))


def display_loss_window():
    window = pygame.display.set_mode((LOSS_WINDOW_WIDTH, LOSS_WINDOW_HEIGHT))
    window.blit(images.loss_window_img, (0, 0))