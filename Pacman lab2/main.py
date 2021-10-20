import pygame
import images
from pacman import Pacman
from common import Position
import app_config
import display
import map
import manhattan_search
import manhattan_search_improved
import all_coins_search
import greedy_heuristics
import through_n_dots_search
import time

pygame.init()
clock = pygame.time.Clock()
images.load_images()
display.init()
pacman = Pacman(app_config.PLAYER_START_POS_X, app_config.PLAYER_START_POS_Y)
map.create_grid(Position(pacman.x, pacman.y))
map.create_coins_map()
destination_cell = map.find_destination_cell()

#path = manhattan_search.manhattan_search(Position(pacman.x, pacman.y), destination_cell)
#path = manhattan_search_improved.manhattan_search_improved(Position(pacman.x, pacman.y), destination_cell)
#path = all_coins_search.all_coins_search(Position(pacman.x, pacman.y), destination_cell)
#path = greedy_heuristics.greedy_heuristics(Position(pacman.x, pacman.y))
path = through_n_dots_search.through_n_dots_search()
time.sleep(2)

while True:
    time.sleep(0.2)
    clock.tick(120)
    pygame.time.delay(80)
    display.display_score()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if len(path) > 0:
        next_position = path.pop(0)
        pacman.walk(next_position)
        pacman.eat_coins()
    display.draw_window()
    display.display_score()
    display.draw_agent(pacman)
    map.spawn_coins()
    display.draw_destination_cell(destination_cell)
    display.update_screen()
