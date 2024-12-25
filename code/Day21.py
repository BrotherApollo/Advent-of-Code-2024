import numpy as np
from copy import deepcopy
import math

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
    
    raise KeyError(f"{item} not found in grid")

def BFS(start:tuple, stop:str, grid:np.array) -> list:
    queue = [[start]]
    checked = []
    solutions = []
    while queue:
        path = queue.pop(0)
        node = path[-1]
        row, col = node
        if grid[row][col] == stop: solutions.append(path)
        if node in checked: continue
        checked.append(node)
        neighbors = [x for x in get_neighbors(node) if valid(x, grid)]
        for neighbor in neighbors:
            nr, nc = neighbor
            if grid[nr][nc] == ".": continue
            new_path = deepcopy(path)
            new_path.append(neighbor)
            queue.append(new_path)
    return [to_arrows(x) for x in solutions]
            
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

# def sort_button(string):
#     counter = {}
#     if "<" in string and "v" in string:
#         first = "<"
#     elif
#     else:
#         first = string[0]
#     for char in string:
#         if counter.get(char):
#             counter[char] += 1
#         else:
#             counter[char] = 1
            
#     output = [first for x in range(counter[first])]
    
#     for key, value in counter.items():
#         if key == first: continue
#         output.extend([key for x in range(value)])
    
#     return "".join(output)

def bot_depth(keys:list):
    output = []
    start = find("A", remote)
    for button in keys:
        # button = sort_button(button)
        # print(button, start)
        for char in button:
            paths = BFS(start, char, remote)
            # paths = filter_paths(paths)
            start = find(char, remote)
            output.append(paths)
        # print(button)
    
    return output

def main(data):
    total = 0
    paths = []
    for code in data:
        start = find('A', keypad)

        print(code)
        value = int(code.strip("A"))
        # print(value)
        for char in code:
            stop = char
            # print(char)
            curr_paths = BFS(start, stop, keypad)
            curr_paths = filter_paths(curr_paths)
            start = find(stop, keypad)
            paths.append(curr_paths)
    # return paths
        for i in range(2):
            paths = [bot_depth(x) for x in paths]
    return paths

    #     # print(''.join(arrows))

    #     answer = ''.join(arrows)
    #     print(len(answer))
    #     total += len(answer) * value
    # print(f"{total}")

def filter_paths(paths):
    best = min([len(x) for x in paths])
    return [x for x in paths if len(x) == best]
    
print(main(["379A"]))
