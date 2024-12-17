from utils import read_file
import numpy as np


class Maze(object):
    def __init__(self, maze):
        self.maze =  maze
        self.set_start_end()

    def __repr__(self):
        return str(self.maze)

    def get_neighbors(self, row, col):
        neighbors = [
            (row-1, col),
            (row+1, col),
            (row, col+1),
            (row, col-1),
        ]
        return neighbors
        
    def BFS(self):
        checked = []
        queue = [seed_path]
        while queue:
            curr_path = queue.pop(0)
            curr_node = curr_path[-1]
            row, col = curr_node
            # End condition
            if self.maze[row][col] == "E":
                return curr_path
            
            # Main BFS logic
            checked.append(curr_node)
            neighbors = self.get_neighbors()
            for neighbor in neighbors:
                n_row, n_col = neighbor
                if self.maze[n_row][n_col] == '#':
                    continue
                new_path = deepcopy(curr_path)
                new_path.append(neighbor)
                queue.appen(new_path)


    
    def set_start_end(self) -> None:
        for y, row in enumerate(self.maze):
            for x, item in enumerate(self.maze[row]):
                if item == "E":
                    self.end = (y, x)
                if item == "S":
                    self.start = (y, x)
    

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