import numpy as np 


test = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<""".split("\n\n")

grid_str = test[0]
movements = test[1]

raw_grid = np.array([list(x) for x in grid_str.split("\n")])

class entitiy():
    def __init__(self, row, col, _type):
        self.row = row
        self.col = col
        self.type = _type
    #     self.grid = grid
    #     self.type = self.lookup()

    # def lookup(self):
    #     value = grid[self.row][self.col]
    #     return value

    def __repr__(self):
        return f"{self.type}"


class Da_Map():
    def __init__(self, raw_grid):
        self.grid = self.build_grid(raw_grid)

    def __repr__(self):
        return str(self.grid)

    def build_grid(self, raw_grid):
        populated_grid = []
        for row, lst in enumerate(raw_grid):
            print(lst)
            new_row = []
            for col, item in enumerate(raw_grid[row]):
                print(item)
                new_row.append(entitiy(
                    row=row,
                    col=col,
                    _type=item,
                ))
            populated_grid.append(new_row)
        return np.array(populated_grid)

Map = Da_Map(raw_grid=raw_grid)
print(Map)