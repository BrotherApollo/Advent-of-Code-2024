import numpy as np
from copy import deepcopy
from collections import defaultdict
from utils import read_file

test = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############""".split("\n")

# maze = np.array([list(x) for x in test])
maze = np.array([list(x) for x in read_file("input/day20.txt")])

print(maze)

class Mazerunner():
    def __init__(self, maze:np.array):
        self.maze = maze
        self.start = self.find("S")
        self.stop = self.find("E")
        self.dists = self.build_dist()
        self.path = self.BFS()
    
    def build_dist(self):
        dists = np.array([[
            -1 for y in range(len(self.maze))
            ] for x in range(len(self.maze[0]))
                  ])
        sr, sc = self.start
        dists[sr][sc] = 0
        return dists

    def find(self, item):
        for row in range(len(self.maze)):
            for col in range(len(self.maze[0])):
                if self.maze[row][col] == item:
                    return (row,col)
                
    def valid(self, point):
        valid = True
        row, col = point
        if row < 0 or row >= len(self.maze):
            valid = False
        if col < 0 or col >= len(self.maze[0]):
            valid = False
        return valid

    def neighbors(self, point):
        row, col = point
        neighbors = [
            (row-1, col),
            (row+1, col),
            (row, col+1),
            (row, col-1),
        ]
        return [x for x in neighbors if self.valid(x)]

    def BFS(self):
        queue = [[self.start]]
        checked = []
        while queue:
            curr = queue.pop(0)
            node = curr[-1]
            if node == self.stop:
                return curr
            if node in checked:
                continue
            checked.append(node)
            row, col = node
            self.maze[row][col] = '0'
            curr_steps = self.dists[row][col]
            for neighbor in self.neighbors(node):
                row, col = neighbor
                value = self.maze[row][col]
                if value == '#':
                    continue
                if self.dists[row][col] == -1:
                    self.dists[row][col] = curr_steps + 1
                new = deepcopy(curr)
                new.append(neighbor)
                queue.append(new)
    
    def cheat_neighbors(self, point, dist=20):
        points = []
        row, col = point
        for nr in range(len(self.maze)):
            for nc in range(len(self.maze[0])):
                row_delta = abs(row-nr)
                col_delta = abs(col-nc)
                if row_delta + col_delta <= dist:
                    points.append((nr, nc))
        return [x for x in points if self.valid(x)]
    
    def dist(self, a, b):
        row = abs(a[0] - b[0])
        col = abs(a[1] - b[1])
        dist = row + col
        return dist
            
    def cheat(self):
        queue = deepcopy(self.path)
        cheats = {}
        while queue:
            node = queue.pop(0)
            cr, cc = node
            curr_steps = self.dists[cr][cc]
            print(f"{curr_steps=}")
            curr_cheats = []
            neighbors = self.cheat_neighbors(node)
            for neighbor in neighbors:
                nr, nc = neighbor
                nsteps = self.dists[nr][nc]
                if nsteps == -1: continue
                cheat_dist = self.dist(node, neighbor)
                diff = int(curr_steps - nsteps) + cheat_dist
                # print(nsteps, diff)
                if diff >= 0: continue
                curr_cheats.append(diff)            
            cheats[int(curr_steps)] = curr_cheats    
        return cheats
                

runner = Mazerunner(maze)
# print(runner.path)
base = len(runner.path) - 1
print(f"{base=}")

print(runner.dists)
cheats = runner.cheat()
# print(cheats)

tally = defaultdict(int)
for point, lst in cheats.items():
    for score in lst:
        if score > -100: continue
        tally[score] += 1
    
print(tally)

print(sum(tally.values()))


# print(runner.cheat_neighbors(runner.start))

# print(runner.dist(runner.start, runner.stop))

