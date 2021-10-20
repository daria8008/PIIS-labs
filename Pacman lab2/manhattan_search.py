import map
from common import Position


def manhattan_search(start, end):
    visited_map = _create_visited_map()
    paths_map = _create_paths_map()

    _dfs(start, end, visited_map, paths_map)
    path = _recreate_path_from_paths_map(start, end, paths_map)
    return path


def _recreate_path_from_paths_map(start, end, paths_map):
    path = [end]
    curr = end
    while paths_map[curr.y][curr.x] != start:
        curr = paths_map[curr.y][curr.x]
        path.append(curr)
    path.append(start)
    path.reverse()
    return path


def _find_adjacent_cells(curr, visited_map):
    adjacent_cells_with_coins = []
    adjacent_cells_without_coins = []

    if not visited_map[curr.y + 1][curr.x]:
        if map.coins_map[curr.y + 1][curr.x]:
            adjacent_cells_with_coins.append(Position(curr.x, curr.y + 1))
        else:
            adjacent_cells_without_coins.append(Position(curr.x, curr.y + 1))
    if not visited_map[curr.y - 1][curr.x]:
        if map.coins_map[curr.y - 1][curr.x]:
            adjacent_cells_with_coins.append(Position(curr.x, curr.y - 1))
        else:
            adjacent_cells_without_coins.append(Position(curr.x, curr.y - 1))
    if not visited_map[curr.y][curr.x + 1]:
        if map.coins_map[curr.y][curr.x + 1]:
            adjacent_cells_with_coins.append(Position(curr.x + 1, curr.y))
        else:
            adjacent_cells_without_coins.append(Position(curr.x + 1, curr.y))
    if not visited_map[curr.y][curr.x - 1]:
        if map.coins_map[curr.y][curr.x - 1]:
            adjacent_cells_with_coins.append(Position(curr.x - 1, curr.y))
        else:
            adjacent_cells_without_coins.append(Position(curr.x - 1, curr.y))

    return adjacent_cells_with_coins + adjacent_cells_without_coins


def _dfs(curr, end, visited_map, paths_map):
    visited_map[curr.y][curr.x] = True
    if curr.x == end.x and curr.y == end.y:
        return True
    else:
        adjacent_cells = _find_adjacent_cells(curr, visited_map)

        for cell in adjacent_cells:
            if not visited_map[cell.y][cell.x]:
                paths_map[cell.y][cell.x] = Position(curr.x, curr.y)
                found = _dfs(cell, end, visited_map, paths_map)
                if found:
                    return True


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


# Map where each cell equals to previous cell's position
# from which you can get to the current cell.
# The purpose of this map is to be able to reproduce full path
# from A to B during bfs/dfs
def _create_paths_map():
    paths_map = []
    for i in range(len(map.grid)):
        paths_map.append([])
        for j in range(len(map.grid[i])):
            paths_map[i].append(None)
    return paths_map
