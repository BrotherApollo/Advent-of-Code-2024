import numpy as np
from copy import deepcopy

data = """169A
279A
540A
869A
789A""".split("\n")

test = """029A
980A
179A
456A
379A""".split("\n")

keypad = [
    ['7','8','9'],
    ['4','5','6'],
    ['1','2','3'],
    ['-','0', 'A']
]

remote = [
    ['.', '^', 'A'],
    ['<', 'v', '>']
]

def valid(point, grid):
    nrows = len(grid)
    ncols = len(grid[0])
    row, col = point
    valid = True
    if row < 0 or row >= nrows:
        valid = False
    if col < 0 or col >= ncols:
        valid = False
    return valid
    
def get_neighbors(point):
    row, col = point
    points = [
        (row - 1, col),
        (row + 1, col), 
        (row, col - 1),
        (row, col + 1),
    ]
    return points

def find(item, grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == item:
                return (row, col)
    
    raise KeyError("item not found in grid")

def BFS(start:tuple, stop:str, grid:np.array) -> list:
    queue = [[start]]
    checked = []
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node in checked: continue
        row, col = node
        if grid[row][col] == stop: return path
        neighbors = [x for x in get_neighbors(node) if valid(x, grid)]
        for neighbor in neighbors:
            nr, nc = neighbor
            if grid[nr][nc] == ".": continue
            # print(grid[nr][nc])
            new_path = deepcopy(path)
            new_path.append(neighbor)
            queue.append(new_path)
            
def to_arrows(presses:list):
    curr = presses[0]
    output = ''
    for item in presses[1:]:
        output += get_dir(curr, item)
        curr = item
    return output + "A"

def get_dir(a, b):
    diff = (a[0]-b[0], a[1]-b[1])
    dirs = {
        (1,0) : "^", 
        (-1,0) : "v",
        (0,1) : "<",
        (0,-1) : ">"
    }
    return dirs[diff]

def sort_button(string):
    # print(string)
    digits = sorted([ord(x) for x in string], reverse=True)
    # print(digits)
    string = [chr(x) for x in digits]
    # print(string)
    return ''.join(string)

def bot_depth(keys:list):
    output = []
    start = find("A", remote)
    for button in keys:
        button = sort_button(button)
        # print(button, start)
        for char in button:
            path = BFS(start, char, remote)
            start = find(char, remote)
            output.append(to_arrows(path))
        # print(button)
    
    return output

total = 0
for code in test:
    start = find('A', keypad)

    arrows = []
    print(code)
    value = int(code.strip("A"))
    # print(value)
    for char in code:
        stop = char
        # print(char)
        path = BFS(start, stop, keypad)
        arrow = to_arrows(path)
        # print(arrow)
        arrows.append(arrow)
        start = find(stop, keypad)

    for i in range(2):
        # print(''.join(arrows))
        arrows = bot_depth(arrows)

    # print(''.join(arrows))

    answer = ''.join(arrows)
    print(len(answer))
    total += len(answer) * value
print(f"{total}")
# print("------------")

temp = '>>^A'
sort_button("<^<v>")
# temp1 = bot_depth(temp)
# temp2 = bot_depth(temp1)
# print(''.join(bot_depth(temp)))
# print(''.join(temp2))
