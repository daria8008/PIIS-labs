from agent import *
import images
import path_finder
from common import Position
from timeit import default_timer as timer


class Ghost(Agent):
    id = None

    def __init__(self, id, x, y):
        super(Ghost, self).__init__(x, y)
        self.id = id

    def walk(self, pacman_pos):
        start_ucs = timer()
        next_position = path_finder.find_paths_by_ucs(Position(self.x, self.y), pacman_pos)
        print("UCS alg", timer() - start_ucs)
        start_bfs = timer()
        next_position_by_bfs = path_finder.find_path_by_bfs(Position(self.x, self.y), pacman_pos)
        print("BFS alg", timer() - start_bfs)
        start_dfs = timer()
        next_position_by_dfs = path_finder.find_path_by_dfs(Position(self.x, self.y), pacman_pos)
        print("DFS alg", timer() - start_dfs, "\n")

        self.x = next_position.x
        self.y = next_position.y

    def get_image(self):
        return images.ghosts_imgs[self.id]
