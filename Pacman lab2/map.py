import app_config
from common import Position
import display
import random
import numpy as np


def is_wall(x, y):
    return grid[y][x] == 0


def create_coins_map():
    global grid
    global coins_map

    coins_map = []
    for i in range(0, len(grid)):
        coins_map.append([])
        for j in range(0, len(grid[i])):
            if grid[i][j] == 1 \
                    and not (i == app_config.PLAYER_START_POS_Y
                             and j == app_config.PLAYER_START_POS_X):
                coins_map[i].append(np.random.choice([True, False], 1, p=[0.3, 0.7]))
            else:
                coins_map[i].append(False)
    return coins_map


def spawn_coins():
    positions = []

    for i in range(0, len(coins_map)):
        for j in range(0, len(coins_map[i])):
            if coins_map[i][j]:
                positions.append(Position(j, i))
    display.draw_coins(positions)


def create_grid(start):
    global grid
    visited_map = np.full((app_config.MAP_HEIGHT, app_config.MAP_WIDTH), False)
    paths_map = np.full((app_config.MAP_HEIGHT, app_config.MAP_WIDTH), None)
    paths_map[start.y][start.x] = start

    find_passages_using_dfs(start, visited_map, paths_map)
    grid = np.zeros((app_config.MAP_HEIGHT, app_config.MAP_WIDTH))
    create_passages(paths_map)
    make_loops_in_maze()
    create_borders()


def _find_adjacent_cells(curr, visited_map):
    adjacent_cells = []

    if curr.y + 2 < app_config.MAP_HEIGHT and not visited_map[curr.y + 2][curr.x]:
        adjacent_cells.append(Position(curr.x, curr.y + 2))
    if curr.y - 2 >= 0 and not visited_map[curr.y - 2][curr.x]:
        adjacent_cells.append(Position(curr.x, curr.y - 2))
    if curr.x + 2 < app_config.MAP_WIDTH and not visited_map[curr.y][curr.x + 2]:
        adjacent_cells.append(Position(curr.x + 2, curr.y))
    if curr.x - 2 >= 0 and not visited_map[curr.y][curr.x - 2]:
        adjacent_cells.append(Position(curr.x - 2, curr.y))
    random.shuffle(adjacent_cells)
    return adjacent_cells


def find_passages_using_dfs(curr, visited_map, paths_map):
    visited_map[curr.y][curr.x] = True
    adjacent_cells = _find_adjacent_cells(curr, visited_map)

    for cell in adjacent_cells:
        if not visited_map[cell.y][cell.x]:
            paths_map[cell.y][cell.x] = Position(curr.x, curr.y)
            find_passages_using_dfs(cell, visited_map, paths_map)


def create_passages(paths_map):
    global grid
    for i in range(0, len(grid), 2):
        for j in range(0, len(grid[i]), 2):
            grid[i][j] = 1
            grid[(paths_map[i][j].y + i) // 2][(paths_map[i][j].x + j) // 2] = 1
            grid[paths_map[i][j].y][paths_map[i][j].x] = 1


def make_loops_in_maze():
    global grid
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == 0:
                grid[i][j] = np.random.choice([0, 1], 1, p=[0.7, 0.3])


def create_borders():
    global grid
    new_grid = np.zeros((len(grid) + 4, len(grid) + 4))

    for i in range(0, len(new_grid)):
        for j in range(0, len(new_grid[i])):
            if i == 0 or i == 1 or i == len(new_grid) - 1 or i == len(new_grid) - 2 or j == 0 or j == 1 or j == len(new_grid) - 1 or j == len(new_grid) - 2:
                new_grid[i][j] = 0
            else:
                new_grid[i][j] = grid[i - 2][j - 2]
    grid = new_grid


def find_destination_cell():
    for j in range(len(grid) - 3, 5, -1):
        if grid[len(grid) - 3][j] == 1:
            return Position(j, len(grid) - 3)


grid = None
coins_map = None
