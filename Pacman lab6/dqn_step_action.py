from map import grid
from common import Position


def dqn_pacman_action(curr, action_item):
    if action_item == 0:
        if grid[curr.y][curr.x + 1] == 1:
            return Position(curr.x + 1, curr.y)
    elif action_item == 1:
        if grid[curr.y][curr.x - 1] == 1:
            return Position(curr.x - 1, curr.y)
    elif action_item == 2:
        if grid[curr.y + 1][curr.x] == 1:
            return Position(curr.x, curr.y + 1)
    else:
        if grid[curr.y - 1][curr.x] == 1:
            return Position(curr.x, curr.y - 1)
    return curr
