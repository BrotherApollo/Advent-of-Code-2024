from utils import read_file
import numpy as np
from copy import deepcopy
import math
from collections import defaultdict


class Cell():
    def __init__(self, point, direction, score):
        self.point = point
        self.direction = direction
        self.score = score

    def __repr__(self):
        return str(self.score)

class Maze(object):
    def __init__(self, maze):
        self.maze =  maze
        self.cells = []
        self.set_start_end()
        self.score = self.Dijkstra()
        print(f"part1 = {self.score}")
        self.seat_count = self.back_track()
        print(f"part2 = {self.seat_count}")

    def __repr__(self):
        return str(self.maze)

    def back_track(self):
        paths = []
        end_seed = [x for x in self.cells if x.point == self.end]
        queue = [end_seed]
        seen = []
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node.point == self.start:
                paths.append(path)
                continue
            row, col = node.point
            print(f"{node.point=}")
            neighbors = [x for x in self.cells if x.point in self.get_neighbors(row, col)]
            neighbors = [x for x in neighbors if x not in seen]
            print(node.score, [x.score for x in neighbors])
            best_neighbors = [x for x in neighbors if x.score < node.score]
            print(f"{best_neighbors=}")
            # best_neighbors = [x for x in neighbors if x.score == best_score]
            seen.append(node)
            print(best_neighbors)
            for neighbor in best_neighbors:
                if neighbor not in seen:
                    print(neighbor)
                    new_path = deepcopy(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
        nodes = self.flatten(paths)
        self.plot_solution([x.point for x in nodes])
        return len(set(nodes))

    def flatten(self, lst):
        output = []
        for item in lst:
            output.extend(item)
        return output

    def get_neighbors(self, row, col):
        neighbors = [
            (row-1, col),
            (row+1, col),
            (row, col+1),
            (row, col-1),
        ]
        return [x for x in neighbors if self.maze[x[0]][x[1]] != "#"]
    
    def Dijkstra(self):
        seen = []
        queue = [x for x in self.cells if x.point == self.start]
        # print(f"{queue=}")
        while queue:
            queue = sorted(queue, key=lambda item: item.score)
            curr = queue.pop(0)
            # print(curr)
            if curr.point == self.end:
                return curr.score
            seen.append(curr)
            row, col = curr.point
            neighbors = [x for x in self.cells if x.point in self.get_neighbors(row, col)]
            # print(f"{neighbors=}")
            for neighbor in neighbors:
                self.set_values(curr, neighbor)
            queue.extend([x for x in neighbors if x not in seen])

    def set_values(self, a, b):
        score = a.score + 1
        b_score = b.score
        direction = a.direction
        # print(b_score, score)
        new_dir = self.get_dir(a,b)
        if direction != new_dir:
            score += 1000
        # print(score)
        if score < b_score:
            print(b, score)
            b.score = score
            b.direction = new_dir
    
    def set_start_end(self) -> None:
        for y, row in enumerate(self.maze):
            for x, item in enumerate(self.maze[y]):
                if item == "E":
                    self.end = (y, x)
                if item == "S":
                    self.start = (y, x)
                    self.cells.append(Cell((y,x), "East", 0))
                elif item != "#":
                    self.cells.append(Cell((y,x), "unknown", math.inf))
                    
    def plot_solution(self, solution):
        maze = deepcopy(self.maze)
        for point in solution:
            # print(point)
            row, col = point
            maze[row][col] = "o"
        print(maze)
            
    
    def get_dir(self, a,b):
        a = a.point
        b = b.point
        diff = (a[0]-b[0], a[1]-b[1])
        # print(diff)
        dirs = {
            (1,0) : "North",
            (0,-1) : "East",
            (-1,0) : "South",
            (0,1) : "West"
        }
        return dirs[diff]



test = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################""".split("\n")

data = read_file("input/day16.txt")

maze = np.array([list(x) for x in test])

da_maze = Maze(maze)
# print(da_maze)

# # print(da_maze.plot_solution(da_maze.solution))
# print(da_maze.maze)
print(da_maze.cells)
# print([x for x in da_maze.cells if x.point == da_maze.end])
print(f"{da_maze.score=}")
print(f"{da_maze.seat_count=}")

spot_check = [(13,6), (12,5), (7,14), (8,15)]
print([x for x in da_maze.cells if x.point in spot_check])
