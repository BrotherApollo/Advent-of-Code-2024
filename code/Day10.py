import numpy as np
test = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""".split("\n")

data = np.array([[int(y) for y in x] for x in test])
print(data)

class Pathfinder():
    def __init__(self, map: np.array):
        self.map = map
        self.trailheads = self.find_start()

    def find_start(self):
        trail_heads = []
        for row in range(len(data)):
            for col in range(len(data[row])):
                if data[row][col] != 0:
                    continue
                trail_heads.append((row, col))

        return trail_heads

    def valid(self, point):
        valid = True
        row, col = point
        if row < 0 or row >=len(self.data):
            valid = False
        if col < 0 or col >=len(self.data[0]):
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

    def BFS(self, point):
        
        pass

pathfinder = Pathfinder(data)
print(pathfinder.__dict__)