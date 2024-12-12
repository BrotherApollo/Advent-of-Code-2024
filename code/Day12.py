from utils import read_file
import numpy as np

 
class Plot(object):
    def __init__(self, symbol, map, starting_point):
        self.symbol = symbol
        self.map =  map
        self.starting_point = starting_point
        self.tiles = self.BFS()
        self.set_stats()

    def __repr__(self):
        return f"A region of {self.symbol} costs: {self.area} * {self.perimeter} = {self.price}"
        
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
    
    def set_stats(self) -> None:
        area = 0
        perimeter = 0
        for tile in self.tiles:
            area += 1
            perimeter += tile.fence
        self.area = area
        self.perimeter = perimeter
        self.price = area * perimeter
            

class Tile():
    def __init__(self, point, map):
        self.point = point
        self.map = map
        self.fence = 0
        self.symbol = Tile.lookup(point, map)

    def __repr__(self):
        # return f"{self.point=}, {self.fence=}, {self.symbol=}"
        return str(self.point)
    
    @staticmethod
    def lookup(point, map):
        row, col = point
        symbol = map[row][col]
        return symbol

    def valid_grid(self, point) -> bool:
        row, col = point
        if row < 0 or row >= len(self.map):
            return False
        if col < 0 or col >= len(self.map[0]):
            return False
        return True
    
    def set_fence(self) -> None:
        fence = 4 - len(self.neighbors)
        if fence:
            self.fence = fence

        fence_dirs = ["north", "south", "east", "west"]
        neighbor_dirs = []
        for neighbor in self.neighbors:
            if neighbor.point[0] > self.point[0]:
                neighbor_dirs.append("south")
            elif neighbor.point[0] < self.point[0]:
                neighbor_dirs.append("north")
            elif neighbor.point[1] > self.point[1]:
                neighbor_dirs.append("east")
            elif neighbor.point[1] < self.point[1]:
                neighbor_dirs.append("west")
        self.fence_dirs = [x for x in fence_dirs if x not in neighbor_dirs]
            

    def set_neighbors(self, neighbors) -> None:
        self.neighbors = neighbors
        self.set_fence()

    def get_neighbors(self) -> list:
        row, col = self.point
        points = [
            (row+1, col),
            (row-1, col), 
            (row, col+1),
            (row, col-1)
        ]
        neighbors = [
            Tile(
                point=point,
                map=self.map
                ) for point in points if self.valid_grid(point)]
        valid_neighbors = [x for x in neighbors if x.symbol == self.symbol]
        self.set_neighbors(valid_neighbors)
        return valid_neighbors

test = """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE""".split("\n")

map = np.array([list(x) for x in test])
# map = np.array([list(x) for x in read_file("input/day12.txt")])

print(map)
big_points = []
plots = []
for row in range(len(map)):
    for col in range(len(map[row])):
        tile = Tile(point=(row,col), map=map)
        if tile.point in big_points:
            # print(f"{tile=} already in a plot")
            continue
        plot = Plot(tile.symbol, map, tile)
        plots.append(plot)
        big_points.extend(plot.points)

# Part 1
# total = 0
# for plot in plots:
#     total += plot.price
#     print(plot)
# print(f"total price: {total}")

# Part 2
for plot in plots:
    points = plot.points
    rows = set([x[0] for x in points])
    cols = set([x[1] for x in points])
    sides = 0

    for row in rows:
        north = False
        south = False
        tiles = [tile for tile in plot.tiles if tile.point[0] == row]
        for tile in tiles:
            if "north" in tile.fence_dirs:
                if not north:
                    sides += 1
                    north = True
                    print(tile.point, 'adding north')
            else:
                north = False
            if "south" in tile.fence_dirs:
                if not south:
                    sides += 1
                    south = True
                    print(tile.point, 'adding south')

            else:
                south = False
    for col in cols:
        east = False
        west = False
        tiles = [tile for tile in plot.tiles if tile.point[1] == col]
        for tile in tiles:
            if "east" in tile.fence_dirs:
                if not east:
                    sides += 1
                    east = True
                    print(tile.point, 'adding east')
            else:
                east = False
            if "west" in tile.fence_dirs:
                if not west:
                    sides += 1
                    west = True
                    print(tile.point, 'adding west')
            else:
                west = False
    print(sides)

    # for col in cols:
    #     filtered_rows = sorted([x[0] for x in points if x[1] == col])
    #     print(filtered_rows)
    
    break