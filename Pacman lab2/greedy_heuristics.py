import map
from common import Position
import sys


def greedy_heuristics(start):
    destinations = create_destinations_array()
    visited_map = _create_visited_map()
    path = [start]
    _dfs(start, find_coin_with_min_heuristic_value(start), destinations, visited_map, path)
    return path


def _find_adjacent_cells(curr, visited_map):
    adjacent_cells = []

    if not visited_map[curr.y + 1][curr.x]:
        adjacent_cells.append(Position(curr.x, curr.y + 1))
    if not visited_map[curr.y - 1][curr.x]:
        adjacent_cells.append(Position(curr.x, curr.y - 1))
    if not visited_map[curr.y][curr.x + 1]:
        adjacent_cells.append(Position(curr.x + 1, curr.y))
    if not visited_map[curr.y][curr.x - 1]:
        adjacent_cells.append(Position(curr.x - 1, curr.y))
    return adjacent_cells


def _dfs(curr, end, destinations, visited_map, path):
    visited_map[curr.y][curr.x] = True
    new_destinations = list(filter(lambda d: (curr.x, curr.y) != (d.x, d.y), destinations))
    destinations.clear()
    destinations += new_destinations
    if len(destinations) == 0:
        return True
    if curr.x == end.x and curr.y == curr.y:
        found = _dfs(curr, find_coin_with_min_heuristic_value(end), destinations, visited_map, path)
        if found:
            return True
        path.append(curr)
    adjacent_cells = _find_adjacent_cells(curr, visited_map)

    for cell in adjacent_cells:
        if not visited_map[cell.y][cell.x]:
            path.append(cell)
            found = _dfs(cell, end, destinations, visited_map, path)
            if found:
                return True
            path.append(curr)


def create_destinations_array():
    destinations = []
    for i in range(len(map.coins_map)):
        for j in range(len(map.coins_map[i])):
            if map.coins_map[i][j]:
                destinations.append(Position(j, i))
    return destinations


def find_coin_with_min_heuristic_value(coin_position):
    heuristic_value = sys.maxsize
    next_coin_position = None
    for i in range(len(map.coins_map)):
        for j in range(len(map.coins_map[i])):
            if map.coins_map[i][j] and i != coin_position.y and j != coin_position.x:
                if abs(coin_position.y - i) + abs(coin_position.x - j) < heuristic_value:
                    heuristic_value = abs(coin_position.y - i) + abs(coin_position.x - j)
                    next_coin_position = Position(j, i)
    return next_coin_position


# Map of visited cells which is used during bfs/dfs
def _create_visited_map():
    visited_map = []
    for i in range(len(map.grid)):
        visited_map.append([])
        for j in range(len(map.grid[i])):
            if map.grid[i][j] == 0:
                visited_map[i].append(True)
            else:
                visited_map[i].append(False)
    return visited_map
