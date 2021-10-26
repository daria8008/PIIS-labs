from collections import namedtuple

Position = namedtuple('Pos', ['x', 'y'])

Evaluations = namedtuple('Eval', ['pos', 'evaluation'])

Ghost_next_step_chance = namedtuple('Chance', ['pos', 'chance'])
