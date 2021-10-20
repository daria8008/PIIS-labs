import pygame
import images
from app_config import *
import state
import map
window = None


def init():
    global window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Pacman")


def draw_window():
    global window
    pygame.draw.rect(window, BLACK, pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
    for i in range(0, len(map.grid)):
        for j in range(0, len(map.grid[i])):
            if map.grid[i][j] == 0:
                pygame.draw.rect(window, BLUE, pygame.Rect(j * cell_size + 3, i * cell_size + 3, cell_size - 6, cell_size - 6))
    pygame.display.update()


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
    textsurface = myfont.render(f'Score: {state.score}', False, YELLOW)
    window.blit(textsurface, (SCORE_POS_X, SCORE_POS_Y))


def draw_destination_cell(position):
    pygame.draw.rect(window, WHITE, pygame.Rect(position.x * cell_size + 3, position.y * cell_size + 3, cell_size - 6, cell_size - 6))
    pygame.display.update()
