from map import coins_map, grid
from common import Position, Ghost_next_step_chance
import random


def _calculate_chance_of_next_pacman_step(ghost_position, pacman_position):
    evaluations = []
    evaluation = 0
    if grid[pacman_position.y + 1][pacman_position.x] == 1:
        evaluation += 1
        if coins_map[pacman_position.y + 1][pacman_position.x]:
            evaluation += 3
        if ghost_position.y == pacman_position.y + 1 and ghost_position.x == pacman_position.x:
            evaluation -= 12
        evaluations.append(evaluation)
    evaluation = 0
    if grid[pacman_position.y][pacman_position.x - 1] == 1:
        evaluation += 1
        if coins_map[pacman_position.y][pacman_position.x - 1]:
            evaluation += 3
        if ghost_position.y == pacman_position.y and ghost_position.x == pacman_position.x - 1:
            evaluation -= 12
        evaluations.append(evaluation)
    evaluation = 0
    if grid[pacman_position.y][pacman_position.x + 1] == 1:
        evaluation += 1
        if coins_map[pacman_position.y][pacman_position.x + 1]:
            evaluation += 3
        if ghost_position.y == pacman_position.y and ghost_position.x == pacman_position.x + 1:
            evaluation -= 12
        evaluations.append(evaluation)
    evaluation = 0
    if grid[pacman_position.y - 1][pacman_position.x] == 1:
        evaluation += 1
        if coins_map[pacman_position.y - 1][pacman_position.x]:
            evaluation += 3
        if ghost_position.y == pacman_position.y - 1 and ghost_position.x == pacman_position.x:
            evaluation -= 12
        evaluations.append(evaluation)

    chance = sum(evaluations) / len(evaluations)
    return Ghost_next_step_chance(Position(ghost_position.x, ghost_position.y), chance)


def expectimax(ghost_position, previous_ghost_position, pacman_position):
    chances_of_next_step = []
    if grid[ghost_position.y + 1][ghost_position.x] == 1 and previous_ghost_position.y != ghost_position.y + 1:
        chances_of_next_step.append(
            _calculate_chance_of_next_pacman_step(Position(ghost_position.x, ghost_position.y + 1), pacman_position))
    if grid[ghost_position.y - 1][ghost_position.x] == 1 and previous_ghost_position.y != ghost_position.y - 1:
        chances_of_next_step.append(
            _calculate_chance_of_next_pacman_step(Position(ghost_position.x, ghost_position.y - 1), pacman_position))
    if grid[ghost_position.y][ghost_position.x + 1] == 1 and previous_ghost_position.x != ghost_position.x + 1:
        chances_of_next_step.append(
            _calculate_chance_of_next_pacman_step(Position(ghost_position.x + 1, ghost_position.y), pacman_position))
    if grid[ghost_position.y][ghost_position.x - 1] == 1 and previous_ghost_position.x != ghost_position.x - 1:
        chances_of_next_step.append(
            _calculate_chance_of_next_pacman_step(Position(ghost_position.x - 1, ghost_position.y), pacman_position))

    random.shuffle(chances_of_next_step)
    return max(chances_of_next_step, key=lambda x: x.chance).pos
