from utils import read_file
import numpy as np

class Maze(object):
    def __init__(self, maze):
        self.maze =  maze
        self.tiles = self.BFS()
        self.filter_count_sides()
        self.set_stats()

    def __repr__(self):
        return str(self.maze)
        
    def BFS(self):
        tiles = []
        checked = []
        queue = [self.starting_point]
        while queue:
            point = queue.pop(0)
            if point.point in checked:
                continue
            checked.append(point.point)
            if point.symbol == self.symbol:
                tiles.append(point)
                queue += point.get_neighbors()
        self.points = [x.point for x in tiles]
        return tiles
    

test = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############""".split("\n")

maze = np.array([list(x) for x in test])

# print(maze)
da_maze = Maze(maze)

print(da_maze)