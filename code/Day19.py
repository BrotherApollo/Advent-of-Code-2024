from copy import deepcopy
from functools import cache


test = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb""".split("\n\n")


@cache
def check_chunk(design):
    if design == "": 
        return 1
    count = 0
    for i in range(min(len(design), maxlen)+1):
        if design[:i] in patterns:
            count += check_chunk(design[i:])
            # print(future, design[i:])
    return count
            
test_designs = test[1].split("\n")
test_towels = [x.strip() for x in test[0].split(", ")]

with open("input/day19.txt", "r") as file:
    patterns, designs = file.read().split("\n\n")
    patterns = [x for x in patterns.split(', ')]
    designs = designs.split('\n')

# print(test_designs, test_towels)
maxlen = max([len(x) for x in patterns])


print(sum([check_chunk(design) for design in designs]))
    
    
