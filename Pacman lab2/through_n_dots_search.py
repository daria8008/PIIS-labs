import manhattan_search_improved
import random
from common import Position
from app_config import dots_count
import map


def generate_n_destinations_cells(n):
    cells = []

    while len(cells) != n:
        x = random.randint(2, len(map.grid) - 2)
        y = random.randint(2, len(map.grid) - 2)
        if map.grid[y][x] == 1:
            cells.append(Position(y, x))
    return cells


def through_n_dots_search():
    cells = generate_n_destinations_cells(dots_count)
    path = []
    for i in range(dots_count - 1):
        path += manhattan_search_improved.manhattan_search_improved(cells[i], cells[i + 1])
    return path
