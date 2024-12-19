import numpy as np
from copy import deepcopy
from utils import read_file

test = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0""".split("\n")

data = read_file("input/day18.txt")
size = 71
grid = np.array([['.' for x in range(size)]for x in range(size)])
print(grid)

def valid(point):
    global size
    valid = True
    row, col = point
    if row < 0 or row >= size:
        valid = False
    if col < 0 or col >= size:
        valid = False
    return valid

def neighbors(point):
    row, col = point
    neighbors = [
        (row-1, col),
        (row+1, col),
        (row, col+1),
        (row, col-1),
    ]
    return [x for x in neighbors if valid(x)]

def BFS(grid):
    global size
    queue = [[(0,0)]]
    checked = []
    while queue:
        # print(len(queue))
        curr = queue.pop(0)
        node = curr[-1]
        # print(node)
        if node == (70,70):
            return curr
        if node in checked:
            continue
        checked.append(node)
        row, col = node
        grid[row][col] = '0'
        for neighbor in neighbors(node):
            row, col = neighbor
            value = grid[row][col]
            if value == '#':
                continue
            new = deepcopy(curr)
            new.append(neighbor)
            queue.append(new)

# Part 1
for point in data[:1024]:
# for point in test[:12]:
    col, row = [int(x) for x in point.split(',')]
    # print(row, col)
    grid[row][col] = '#'
path = BFS(grid)
print(f"part1 = {len(path)-1}")

# with open('output.txt', 'w') as file:
#     for row in grid:
#         file.write(str(''.join(row))+"\n")

# Part 2
for point in data[1024:]:
    col, row = [int(x) for x in point.split(',')]
    grid[row][col] = '#'
    if (row, col) in path:
        # print(col, row)
        path = BFS(grid)
        if not path:
            print(f"{row=}, {col=}")