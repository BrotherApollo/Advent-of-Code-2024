import numpy as np
import re
from utils import read_file

class Bot():
    def __init__(self, row, col, dcol, drow):
        self.col = col
        self.row = row
        self.dcol = dcol
        self.drow = drow
    
    def move(self):
        self.row += self.drow
        self.col += self.dcol
        # converting to a 0 range
        
        if self.col < 0:
            self.col += WIDTH
        elif self.col >= WIDTH:
            self.col -= WIDTH
        
        if self.row < 0:
            self.row += HEIGHT
        elif self.row >= HEIGHT:
            self.row -= HEIGHT        
        
    def __repr__(self):
        return str(self.__dict__)
            
    @staticmethod
    def parse(string) -> "Bot":
        data = re.findall(r"(\d{1,}|-\d{1,})", string)
        "p=0,4 v=3,-3"        
        stats = []
        for item in data:
            if '-' in item:
                stats.append(int(item.strip("-")) * -1)
            else:
                stats.append(int(item))
        return Bot(
            col=stats[0],
            row=stats[1],
            dcol= stats[2],
            drow=stats[3]
            )
                           
    
class Da_Map():
    def __init__(self, bot_data):
        self.height = HEIGHT
        self.width = WIDTH
        self.bots = self.add_bots(bot_data)
        
    def __repr__(self):
        return str(self.grid)
    
    def score(self):
        self.grid = self.build_grid()
        self.place_bots()
        totals = []
        final = 0
        quads = self.quads()
        for quad in quads:
            nums = []
            for row in quad:
                nums += [int(x) for x in row if x != '.']
            score = sum(nums)
            totals.append(sum(nums))
            if final:
                final = final * score
            else:
                final = score        
        return final
    
    def quads(self):
        mid_col = WIDTH - WIDTH//2
        mid_row = HEIGHT - HEIGHT//2
        
        quads = [self.grid[:mid_row-1, :mid_col-1],  # top left
                 self.grid[:mid_row-1, mid_col:],  # top right
                 self.grid[mid_row:, :mid_col-1],  # bottom left
                 self.grid[mid_row:, mid_col:]  # bottom right
        ]
        return quads
    
    def next_second(self):
        for bot in self.bots:
            bot.move()
    
    def place_bots(self):
        for bot in self.bots:
            cell = self.grid[bot.row][bot.col]
            if cell == '.':
                cell = 1
            else:
                cell = int(cell)
                cell += 1
            self.grid[bot.row][bot.col] = cell

    def build_grid(self):
        grid = np.array(
            [['.' for y in range(self.width)]
        for x in range(self.height)]
                    )
        return grid

    def add_bots(self, bot_data):
        bots = []
        for string in bot_data:
            bots.append(Bot.parse(string))
        return bots

HEIGHT = 103
WIDTH = 101

# BOTS = """p=0,4 v=3,-3
# p=6,3 v=-1,-3
# p=10,3 v=-1,2
# p=2,0 v=2,-1
# p=0,0 v=1,3
# p=3,0 v=-2,-2
# p=7,6 v=-1,-3
# p=3,0 v=-1,-2
# p=9,3 v=2,3
# p=7,3 v=-1,2
# p=2,4 v=2,-3
# p=9,5 v=-3,-3""".split("\n")

BOTS = read_file("input/day14.txt")
# print(BOTS)
# Bot.parse(BOTS[0])
map = Da_Map(BOTS)
# print(map.bots)
# print(map)
for i in range(100):
    map.next_second()
    # print(map)
# print(map)
print(map.score())
