from utils import read_file
import numpy as np

 
class Plot(object):
    def __init__(self, symbol, map, starting_point):
        self.symbol = symbol
        self.map =  map
        self.starting_point = starting_point
        self.tiles = self.BFS()
        self.filter_count_sides()
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
        self.part1_price = area * perimeter
        self.part2_price = area * self.sides

    def filter_count_sides(self):
        rows = set([x[0] for x in self.points])
        cols = set(x[1] for x  in self.points)
        north_fences = []
        south_fences = []
        west_fences = []
        east_fences = []
        for row in rows:
            curr_row = [tile for tile in self.tiles if tile.point[0] == row]
            north_fences.append(sorted(
                [x for x in curr_row if "north" in x.fence_dirs],
                key=lambda x : x.point[1])
                )
            south_fences.append(sorted(
                [x for x in curr_row if "south" in x.fence_dirs],
                key=lambda x : x.point[1])
                )
        for col in cols:
            curr_col = [tile for tile in self.tiles if tile.point[1] == col]
            west_fences.append(
                sorted([x for x in curr_col if "west" in x.fence_dirs],
                key=lambda x : x.point[0])
                )
            east_fences.append(sorted(
                [x for x in curr_col if "east" in x.fence_dirs],
                key=lambda x : x.point[0])
                )
        sides = sum([
            self.sets(north_fences),
            self.sets(south_fences),
            self.sets(east_fences),
            self.sets(west_fences)
        ])
        self.sides = sides
    
    def sets(self, groups):
        sides = 0
        for group in groups:
            queue = group
            seen = []
            # sides = 0
            while queue:
                curr = queue.pop(0)
                if curr in seen:
                    continue
                seen.append(curr.point)
                bool_bag = [neighbor.point in seen for neighbor in curr.neighbors]
                if any(bool_bag):
                    continue
                sides += 1

        return sides
            

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
    

test = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE""".split("\n")

# map = np.array([list(x) for x in test])
map = np.array([list(x) for x in read_file("input/day12.txt")])

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

#Part 1
part1_total = 0
for plot in plots:
    part1_total += plot.part1_price
print(part1_total)

# Part 2
part2_total = 0
for plot in plots:
    part2_total += plot.part2_price
print(part2_total, "805814")
