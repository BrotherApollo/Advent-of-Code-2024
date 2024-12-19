import numpy as np 
from copy import deepcopy

test = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^""".split("\n\n")

with open("input/day15.txt", "r") as file:
    data = file.read().split("\n\n")
    
grid_str = data[0]
commands = [x for x in data[1] if x != "\n"]

raw_grid = np.array([list(x) for x in grid_str.split("\n")])

class Bot():
    def __init__(self, row, col, _type):
        self.row = row
        self.col = col
        self.type = _type
        self.point = (row, col)

    def __repr__(self):
        return f"{self.type}"
    
    def move(self, delta):
        drow, dcol = delta
        row = self.row + drow
        col = self.col + dcol
        self.row = row
        self.col = col
        self.point = (row, col)
    

class Da_Map():
    def __init__(self, raw_grid, commands):
        self.grid = self.build_grid(raw_grid)
        self.bot_commands = commands
        self.steps()
        self.score = self.score_state()

    def __repr__(self):
        grid = deepcopy(self.grid)
        row, col = self.bot.point
        grid[row][col] = '@'
        return str(grid)
    
    def score_state(self):
        GPS_pos = []
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col] != 'O':
                    continue
                gps = 100 * row + col
                GPS_pos.append(gps)
                
        print(GPS_pos)
        return sum(GPS_pos)
    
    def steps(self):
        count = 0
        for step in self.bot_commands:
            count+=1
            new_point = self.next_cell(self.bot.point, step)
            cell = self.grid[new_point[0]][new_point[1]]
            delta = self.get_dir(step)
            if cell == ".":
                self.bot.move(delta)
            elif cell == "O":
                shift = self.shift_package(step, new_point) 
                if shift:
                    self.bot.move(delta)
            print(count)
            # print(self)           
            # print(step, delta, cell, count)
    
    def shift_package(self, step, point):
        row, col = self.next_cell(point, step)
        _type = self.grid[row][col]
        if _type == '.':
            self.grid[row][col] = "O"
            old_row, old_col = point
            self.grid[old_row][old_col] = "."
            return True
        elif _type == "O":
            shift = self.shift_package(step, (row, col))
            if shift:
                self.grid[row][col] = "O"
                old_row, old_col = point
                self.grid[old_row][old_col] = "."
            return shift
                
    def next_cell(self, point, dir):
        delta = self.get_dir(dir)
        row, col = point
        new_point = (row+delta[0], col+delta[1])
        return new_point
    
    def get_dir(self, symbol):
        dir_dict = {
            "^": (-1, 0),
            ">": (0, 1),
            "<": (0, -1),
            "v": (1, 0)
        }
        return dir_dict[symbol]

    def build_grid(self, raw_grid):
        populated_grid = []
        for row, lst in enumerate(raw_grid):
            new_row = []
            for col, item in enumerate(raw_grid[row]):
                if item == "@":
                    self.bot = Bot(
                    row=row,
                    col=col,
                    _type=item,
                )
                    new_row.append('.')
                else:
                    new_row.append(item)
            populated_grid.append(new_row)
        return np.array(populated_grid)

Map = Da_Map(raw_grid=raw_grid, commands=commands)
print(Map)
print(Map.score)
