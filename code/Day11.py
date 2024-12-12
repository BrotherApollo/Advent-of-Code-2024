from utils import read_file
from collections import defaultdict
from copy import deepcopy

def blink(stones:defaultdict) -> defaultdict:
    new_stones = defaultdict(int)

    if 0 in stones:
        new_stones[1] = stones[0]
        del stones[0]
    # Iterate over the rest
    for stone, count in stones.items():
        str_stone = str(stone)
        if (length:= len(str_stone)) % 2 == 0:
            mid = length // 2
            left = int(str_stone[:mid])
            right = int(str_stone[mid:])
            new_stones[left] += count
            new_stones[right] += count
        else:
            num = stone *2024
            new_stones[num] += count

    return new_stones


data = read_file("input/day11.txt")
stones = defaultdict(int)
for item in data[0].split(' '):
    stones[int(item)] += 1

for i in range(75):
    if i == 25:
        part1 = sum(stones.values())
    new_stones = blink(stones)
    stones = deepcopy(new_stones)
part2 = sum(stones.values())

print(f"{part1=}, {part2=}")