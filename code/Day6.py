from utils import read_file
import numpy as np
from copy import deepcopy

def make_matrix(filepath:str) -> np.array:
    lines = read_file(filepath)
    return np.array([list(line) for line in lines ])

test = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".split("\n")

class Roomba(object):
    def __init__(self, matrix, y, x):
        self.matrix = deepcopy(matrix)
        self.y = y
        self.x = x
        self.curr_dir = 'up'
        self.loop = False
        self.directions={
            'up': {'turn':'right', 'delta': {'y':-1, 'x':0}},
            'right': {'turn':'down', 'delta': {'y':0, 'x':+1}},
            'down': {'turn':'left', 'delta': {'y':+1, 'x':0}},
            'left': {'turn':'up', 'delta': {'y':0, 'x':-1}},
        }
        
    def turn(self):
        self.curr_dir = self.directions[self.curr_dir]["turn"]
    
    def coutem(self):
        positions = 0
        matrix = self.matrix
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if matrix[y][x] == "X":
                    positions += 1
        return positions
    
    def step(self, dx, dy):
        if self.on_map():
            self.matrix[self.y][self.x] = "X"
            self.x += dx
            self.y += dy

    def check_for_obs(self, y, x):
        try: 
            return self.matrix[y][x] == "#"
        except IndexError:
            return False

    def on_map(self) -> bool:
        we_good = True
        if self.x < 0 or self.x >= len(self.matrix[0]):
            we_good = False
        if self.y < 0 or self.y >= len(self.matrix):
            we_good = False
        # print(f"we good? {we_good}")
        return we_good
    
    def roomba(self) -> np.array:
        count = 0
        while self.on_map():
            if count > 100000:
                self.loop = True
                break
            count += 1
            dy = self.directions[self.curr_dir]["delta"]["y"]
            dx = self.directions[self.curr_dir]["delta"]["x"]
            if self.check_for_obs(y= self.y + dy, x= self.x + dx):
                # print("we turnin")
                self.turn()
            else:
                self.step(dx, dy)
        self.count = self.coutem()
        return self.matrix



matrix = make_matrix("input/day6.txt")
# matrix = np.array([list(x) for x in test])
for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        curr = matrix[y][x]
        if curr == '^':
            startx=x
            starty=y
roomba = Roomba(matrix, x=startx, y=starty)
output = roomba.roomba()
print(output)
print(roomba.count)


# Slam this CPU
loops = 0

for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        item = matrix[y][x]
        if item == '.':
            new_matrix = deepcopy(matrix)
            new_matrix[y][x] = '#'
            # print(new_matrix)
            x = Roomba(new_matrix, x=startx, y=starty)
            x.roomba()
            if x.loop:
                loops +=1
                print("found one")
                
print(loops)