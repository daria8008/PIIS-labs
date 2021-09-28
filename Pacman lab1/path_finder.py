import heapq
from map import grid
from common import Position, Priority_queue_item


def find_path_by_bfs(start, end):
    visited_map = _create_visited_map()
    paths_map = _create_paths_map()
    queue = [start]
    found = False

    while not found:
        curr = queue.pop(0)
        visited_map[curr.y][curr.x] = True
        if curr.x == end.x and curr.y == end.y:
            found = True
        else:
            if not visited_map[curr.y + 1][curr.x]:
                queue.append(Position(curr.x, curr.y + 1))
                paths_map[curr.y + 1][curr.x] = Position(curr.x, curr.y)
            if not visited_map[curr.y - 1][curr.x]:
                queue.append(Position(curr.x, curr.y - 1))
                paths_map[curr.y - 1][curr.x] = Position(curr.x, curr.y)
            if not visited_map[curr.y][curr.x + 1]:
                queue.append(Position(curr.x + 1, curr.y))
                paths_map[curr.y][curr.x + 1] = Position(curr.x, curr.y)
            if not visited_map[curr.y][curr.x - 1]:
                queue.append(Position(curr.x - 1, curr.y))
                paths_map[curr.y][curr.x - 1] = Position(curr.x, curr.y)
    return _found_first_cell_in_paths(start, end, paths_map)


def _found_first_cell_in_paths(start, end, paths_map):
    curr = end
    while paths_map[curr.y][curr.x] != start:
        curr = paths_map[curr.y][curr.x]
    return curr


def find_path_by_dfs(start, end):
    visited_map = _create_visited_map()
    paths_map = _create_paths_map()

    dfs(start, end, visited_map, paths_map)
    return _found_first_cell_in_paths(start, end, paths_map)


def dfs(curr, end, visited_map, paths_map):
    visited_map[curr.y][curr.x] = True
    if curr.x == end.x and curr.y == end.y:
        return True
    else:
        if not visited_map[curr.y][curr.x - 1]:
            paths_map[curr.y][curr.x - 1] = Position(curr.x, curr.y)
            found = dfs(Position(curr.x - 1, curr.y), end, visited_map, paths_map)
            if found:
                return True
        if not visited_map[curr.y + 1][curr.x]:
            paths_map[curr.y + 1][curr.x] = Position(curr.x, curr.y)
            found = dfs(Position(curr.x, curr.y + 1), end, visited_map, paths_map)
            if found:
                return True
        if not visited_map[curr.y][curr.x + 1]:
            paths_map[curr.y][curr.x + 1] = Position(curr.x, curr.y)
            found = dfs(Position(curr.x + 1, curr.y), end, visited_map, paths_map)
            if found:
                return True
        if not visited_map[curr.y - 1][curr.x]:
            paths_map[curr.y - 1][curr.x] = Position(curr.x, curr.y)
            found = dfs(Position(curr.x, curr.y - 1), end, visited_map, paths_map)
            if found:
                return True


def find_paths_by_ucs(start, end):
    visited_map = _create_visited_map()
    paths_map = _create_paths_map()
    priority_queue = [Priority_queue_item(0, start)]
    found = False

    while not found:
        curr = heapq.heappop(priority_queue)

        visited_map[curr.position.y][curr.position.x] = True
        if curr.position.x == end.x and curr.position.y == end.y:
            found = True
        else:
            if not visited_map[curr.position.y + 1][curr.position.x]:
                heapq.heappush(priority_queue, Priority_queue_item(curr.distance + 1, Position(curr.position.x, curr.position.y + 1)))
                paths_map[curr.position.y + 1][curr.position.x] = Position(curr.position.x, curr.position.y)
            if not visited_map[curr.position.y - 1][curr.position.x]:
                heapq.heappush(priority_queue, Priority_queue_item(curr.distance + 1, Position(curr.position.x, curr.position.y - 1)))
                paths_map[curr.position.y - 1][curr.position.x] = Position(curr.position.x, curr.position.y)
            if not visited_map[curr.position.y][curr.position.x + 1]:
                heapq.heappush(priority_queue, Priority_queue_item(curr.distance + 1, Position(curr.position.x + 1, curr.position.y)))
                paths_map[curr.position.y][curr.position.x + 1] = Position(curr.position.x, curr.position.y)
            if not visited_map[curr.position.y][curr.position.x - 1]:
                heapq.heappush(priority_queue, Priority_queue_item(curr.distance + 1, Position(curr.position.x - 1, curr.position.y)))
                paths_map[curr.position.y][curr.position.x - 1] = Position(curr.position.x, curr.position.y)
    return _found_first_cell_in_paths(start, end, paths_map)


# Map of visited cells which is used during bfs/dfs
def _create_visited_map():
    visited_map = []
    for i in range(len(grid)):
        visited_map.append([])
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
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
    for i in range(len(grid)):
        paths_map.append([])
        for j in range(len(grid[i])):
            paths_map[i].append(None)
    return paths_map
