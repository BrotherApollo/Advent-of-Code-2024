# Standard imports
import os

# Local Imports
from utils import read_file

def parse_input(path:str):
    lines = read_file(path)
    left = []
    right = []
    for line in lines:
        left_temp, right_temp = [int(x) for x in line.split(" ") if x]
        left.append(left_temp)
        right.append(right_temp)
    return (left, right)

def calculate_difference(left:list, right:list) -> int:
    l_set = sorted(left)
    r_set = sorted(right)
    sumodiff = 0
    for index in range(len(l_set)):
        sumodiff += abs(l_set[index] - r_set[index])
    return sumodiff

def similarity(left:list, right:list) -> int:
    score = 0
    for item in left:
        filtered = [x for x in right if x==item]
        score += item* len(filtered)
    return score

left, right = parse_input("input/day1.txt")

# Part One
diff = calculate_difference(left=left, right=right)
print(diff)

# Part Two
sim = similarity(left=left, right=right)
print(sim)