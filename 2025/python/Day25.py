from utils import read_file
import numpy as np

with open("input/day25.txt", "r") as file:
    data = file.read().split("\n\n")
# print(data)

test = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####""".split("\n\n")

locks = []
keys = []

for item in data:
    
    matrix = np.array([list(x) for x in item.split("\n") if x])
    nums =[]
    for col in range(5):
        height = 0
        for row in matrix[1:-1]:
            if row[col] == "#": height+=1 
        nums.append(height)
    print(nums)
    nums = np.array(nums)
    if all([x == "#" for x in matrix[0]]):
        locks.append(nums)
    else:
        keys.append(nums)
    
print(locks, keys, sep = "\n\n")


total = 0
for lock in locks:
    for key in keys:
        sums = lock + key
        bool_bag = [x<=5 for x in sums]
        print(bool_bag)
        if all(bool_bag):
            total += 1
        print(sums)
print(total)