import map
from common import Position


def all_coins_search(start, end):
    visited_map = _create_visited_map()
    path = []
    destinations = create_destinations_array(start, end)

    _dfs(start, destinations, visited_map, path)
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


def _dfs(curr, destinations, visited_map, path):
    visited_map[curr.y][curr.x] = True
    new_destinations = list(filter(lambda d: (curr.x, curr.y) != (d.x, d.y), destinations))
    destinations.clear()
    destinations += new_destinations
    if len(destinations) == 0:
        return True

    adjacent_cells = _find_adjacent_cells(curr, visited_map)

    for cell in adjacent_cells:
        if not visited_map[cell.y][cell.x]:
            path.append(cell)
            found = _dfs(cell, destinations, visited_map, path)
            if found:
                return True
            path.append(curr)


def create_destinations_array(start, end):
    destinations = [start, end]
    for i in range(len(map.coins_map)):
        for j in range(len(map.coins_map[i])):
            if map.coins_map[i][j]:
                destinations.append(Position(j, i))
    return destinations


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
