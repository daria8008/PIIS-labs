from collections import namedtuple

Position = namedtuple('Pos', ['x', 'y'])

Ghost_next_step_chance = namedtuple('Chance', ['pos', 'chance'])
