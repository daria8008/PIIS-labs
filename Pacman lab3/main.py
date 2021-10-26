import pygame
import images
from pacman import Pacman
from ghost import Ghost
from common import Position
import app_config
import display
import map
from timeit import default_timer as timer
import state


def check_game_end():
    for i in range(len(map.coins_map)):
        for j in range(len(map.coins_map[i])):
            if map.coins_map[i][j] == 1:
                return False
    return True


def check_pacman_die():
    for ghost in ghosts:
        if ghost.x == pacman.x and ghost.y == pacman.y:
            return True
    return False


pygame.init()
clock = pygame.time.Clock()

images.load_images()
display.init()

run = True
pacman = Pacman(app_config.PLAYER_START_POS_X, app_config.PLAYER_START_POS_Y)

ghosts = []

for i in range(app_config.enemies_cnt):
    (posX, posY) = app_config.ghosts_start_positions[i]
    ghosts.append(Ghost(i, posX, posY, 0, 0))
algorithm = ' minimax'
# algorithm = ' expectimax'
start = timer()


while run:
    clock.tick(120)
    pygame.time.delay(80)

    if check_game_end():
        f = open('statistics.csv', 'a').write('win ' + str(timer() - start) + ' ' + str(state.score) + algorithm + '\n')
        while run:
            display.display_win_window()
            display.update_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
    if check_pacman_die():
        f = open('statistics.csv', 'a').write('loss ' + str(timer() - start) + ' ' + str(state.score) + algorithm + '\n')
        while run:
            display.display_loss_window()
            display.update_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

    display.display_score()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            f = open('statistics.csv', 'a').write('not_finished ' + str(timer() - start) + ' ' + str(state.score) +
                                                  str(algorithm) + '\n')
            run = False

    pacman.walk(ghosts)
    pacman.eat_coins()

    for ghost in ghosts:
        ghost.walk_optimal(Position(pacman.x, pacman.y))
        #ghost.walk_random(Position(pacman.x, pacman.y))

    display.draw_window()
    display.display_score()
    display.draw_agent(pacman)
    map.spawn_coins()

    for ghost in ghosts:
        display.draw_agent(ghost)
    display.update_screen()
