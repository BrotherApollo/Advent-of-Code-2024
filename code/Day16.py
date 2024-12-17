from utils import read_file
import numpy as np
from copy import deepcopy
import math


class Maze(object):
    def __init__(self, maze):
        self.maze =  maze
        self.set_start_end()
        self.solutions = self.BFS()
        self.score = self.score_solutions()

    def __repr__(self):
        return str(self.maze)

    def get_neighbors(self, row, col):
        neighbors = [
            (row-1, col),
            (row+1, col),
            (row, col+1),
            (row, col-1),
        ]
        return [x for x in neighbors if self.maze[x[0]][x[1]] != "#"]
    
    def Dijkstra(self):
        queue = []
    
    
    def set_start_end(self) -> None:
        for y, row in enumerate(self.maze):
            for x, item in enumerate(self.maze[y]):
                if item == "E":
                    self.end = (y, x)
                if item == "S":
                    self.start = (y, x)
                    
    def plot_solution(self, solution):
        maze = deepcopy(self.maze)
        for point in solution:
            # print(point)
            row, col = point
            maze[row][col] = "o"
        print(maze)
            
    
    def get_dir(self, a,b):
        diff = (a[0]-b[0], a[1]-b[1])
        # print(diff)
        dirs = {
            (1,0) : "North",
            (0,-1) : "East",
            (-1,0) : "South",
            (0,1) : "West"
        }
        return dirs[diff]



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

data = read_file("input/day16.txt")

maze = np.array([list(x) for x in data])

da_maze = Maze(maze)
print(da_maze)

# # print(da_maze.plot_solution(da_maze.solution))
print(da_maze.score)
