from utils import read_file

from copy import deepcopy

def parse_file(filename):
    lines = read_file(filename)
    data = [[int(x) for x in line.split(" ")] for line in lines]

    return data


def check_safe(data: list[int]) -> bool:
    increasing = False
    decreasing = False
    for i in range(len(data)-1):
        first, second = data[i:i+2]
        if first - second < 0:
            decreasing = True
        if first - second > 0:
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
# Part one
Unsafe = 0
Safe = 0 
for line in data:
    if check_safe(line):
        Safe +=1
    else:
        Unsafe += 1

# print(Safe)

# Part 2
Unsafe = 0
Safe = 0 
for line in data:
    if check_safe(line):
        Safe += 1
    elif remove_one(line):
        Safe += 1
    else:
        Unsafe += 1

print(Safe)