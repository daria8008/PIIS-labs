from map import coins_map, grid
from common import Evaluations, Position
from operator import attrgetter
import random


def minimax(curr, ghosts):
    evaluations = []
    evaluation = 0
    if grid[curr.y + 1][curr.x] == 1:
        evaluation += 1
        if coins_map[curr.y + 1][curr.x]:
            evaluation += 3
        for ghost in ghosts:
            if ghost.y == curr.y + 1 and ghost.x == curr.x:
                evaluation -= 12
        evaluations.append(Evaluations(Position(curr.x, curr.y + 1), evaluation))
    evaluation = 0
    if grid[curr.y][curr.x - 1] == 1:
        evaluation += 1
        if coins_map[curr.y][curr.x - 1]:
            evaluation += 3
        for ghost in ghosts:
            if ghost.y == curr.y and ghost.x == curr.x - 1:
                evaluation -= 12
        evaluations.append(Evaluations(Position(curr.x - 1, curr.y), evaluation))
    evaluation = 0
    if grid[curr.y][curr.x + 1] == 1:
        evaluation += 1
        if coins_map[curr.y][curr.x + 1]:
            evaluation += 3
        for ghost in ghosts:
            if ghost.y == curr.y and ghost.x == curr.x + 1:
                evaluation -= 12
        evaluations.append(Evaluations(Position(curr.x + 1, curr.y), evaluation))
    evaluation = 0
    if grid[curr.y - 1][curr.x] == 1:
        evaluation += 1
        if coins_map[curr.y - 1][curr.x]:
            evaluation += 3
        for ghost in ghosts:
            if ghost.y == curr.y - 1 and ghost.x == curr.x:
                evaluation -= 12
        evaluations.append(Evaluations(Position(curr.x, curr.y - 1), evaluation))

    random.shuffle(evaluations)
    evaluations = sorted(evaluations, key=attrgetter('evaluation'))
    return evaluations[len(evaluations) - 1].pos
