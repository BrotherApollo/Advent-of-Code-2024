import numpy as np
from copy import deepcopy
from utils import read_file

test = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""".split("\n")

# data = np.array([[int(y) for y in x] for x in test])
# print(data)
data = np.array([[int(y) for y in x] for x in read_file("input/day10.txt")])

class Trail():
    def __init__(self, trailhead, paths):
        self.trailhead = trailhead
        self.paths = paths
        self.score = self.count_nines()
        self.rating = len(self.paths)

    def count_nines(self):
        nines = [x[-1] for x in self.paths]
        return len(set(nines))
    
    def __repr__(self):
        return f"{self.trailhead}: raw count:{len(self.paths)}, score: {self.score}"

class Pathfinder():
    def __init__(self, map: np.array):
        self.map = map
        self.trailheads = self.find_start()
        # self.trailheads = [(0,2)]
        self.trails = self.find_trails()
        self.total_score = self.total_score()
        self.total_rating = self.total_rating()

    def total_rating(self):
        total = 0
        for trail in self.trails:
            total += trail.rating
        return total 
    
    def total_score(self):
        total = 0
        for trail in self.trails:
            total += trail.score
        return total

    def find_trails(self):
        trails = []
        for trailhead in self.trailheads:
            temp = self.BFS(trailhead)
            trails.append(Trail(trailhead=trailhead, paths=temp))
        return trails

    def find_start(self):
        trail_heads = []
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                if self.map[row][col] != 0:
                    continue
                trail_heads.append((row, col))

        return trail_heads

    def valid(self, point):
        valid = True
        row, col = point
        if row < 0 or row >=len(self.map):
            valid = False
        if col < 0 or col >=len(self.map[0]):
            valid = False
        return valid

    def get_neighbors(self, point):
        row, col = point
        neighbors = [
            (row+1, col), 
            (row-1, col),
            (row, col+1),
            (row, col-1)
        ]
        return [x for x in neighbors if self.valid(x)]

    def get_value(self, point):
        row, col = point
        value = self.map[row][col]
        return value

    def BFS(self, point):
        starting_path = [point]
        que = [starting_path]
        visited = []
        valid_paths = []
        while que:
            path = que.pop(0)
            curr_pos = path[-1]
            visited.append(curr_pos)
            curr_value = self.get_value(curr_pos)
            if curr_value == 9:
                # print(f"found path {curr_value=}, ")
                valid_paths.append(path)
            neighbors = self.get_neighbors(curr_pos)
            for neighbor in neighbors:
                neighbor_value = self.get_value(neighbor)
                if neighbor_value == curr_value + 1:
                    new_path = deepcopy(path)
                    new_path.append(neighbor)
                    que.append(new_path)
                    print(new_path)
        return valid_paths

pathfinder = Pathfinder(data)
print(pathfinder.__dict__)