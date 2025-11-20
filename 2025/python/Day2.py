# Standard Imports
from copy import deepcopy
#Local Imports
from utils import read_file


def parse_file(filename):
    lines = read_file(filename)
    data = [[int(x) for x in line.split(" ")] for line in lines]

    return data


def check_safe(data: list[int]) -> bool:
    increasing = False
    decreasing = False
    for i in range(len(data)-1):
        first, second = data[i:i+2]
        if first - second > 0:
            decreasing = True
        if first - second < 0:
            increasing = True

        if abs(first - second) > 3:
            return False
        if abs(first - second) < 1:
            return False

    if increasing and decreasing:
        return False
    return True


def remove_one(line: list[int]) -> bool:
    for index in range(len(line)):
        new_line = deepcopy(line)
        new_line.pop(index)
        if check_safe(new_line):
            return True
    return False
        
data = parse_file("input/day2.txt")
Unsafe = 0
Safe = 0 
Kinda_safe = 0
for line in data:
    if check_safe(line):
        Safe += 1
        Kinda_safe += 1
    elif remove_one(line):
        Kinda_safe += 1
    else:
        Unsafe += 1

# Safe is the answer for part one, Kinda Safe is for Part two
print(f"{Safe=}, {Kinda_safe=}")