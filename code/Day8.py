from utils import read_file
import numpy as np
from copy import deepcopy

data = np.array([list(x) for x in read_file("input/day8.txt")])
test = np.array([list(x) for x in """.....
..a..
..a..
..b..
..b..
.....""".replace("#",".").split("\n")])
# print(test)


def map_grids(matrix):
    dic = {}
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            cell = matrix[row][col]
            if cell == '.':
                continue
            if dic.get(cell):
                dic[cell].append((row,col))
            else:
                dic[cell] = [(row, col)]
    return dic

def get_diff(a:tuple, b:tuple):
    row = a[0] - b[0]
    col = a[1] - b[1]
    return (row, col)

def rippem(node, diff, up=True):
    nodes = []
    row,col = node
    while validate_node((row,col)):
        if up:
            row += diff[0]
            col += diff[1]
        else:
            row -= diff[0]
            col -= diff[1]
        nodes.append((row,col))
    return nodes

def find_anitnode(a:tuple, b:tuple):
    diff = get_diff(a,b)
    print(f"{diff=}")
    nodes = [a,b]
    #up
    nodes += rippem(a, diff, True)
    nodes += rippem(a, diff, False)
    print(f"{nodes=}")
    # return [x for x in nodes if x not in (a,b)]
    return nodes

def validate_node(node):
    global matrix
    valid = True
    if node[0] < 0 or node[0] >= len(matrix):
        valid = False
    if node[1] < 0 or node[1] >= len(matrix[0]):
        valid = False
    # print(valid)
    return valid

matrix = data

dic = map_grids(matrix)

anitnodes = []
for key in dic.keys():
    que = deepcopy(dic[key])
    while que:
        print(que)
        a = que.pop(0)
        for b in que:
            print(a,b)
            anitnodes += find_anitnode(a,b)

anitnodes = [x for x in anitnodes if validate_node(x)]
print(len(anitnodes))
print(len(set(anitnodes)))

# print(anitnodes)
# print(dic.keys())