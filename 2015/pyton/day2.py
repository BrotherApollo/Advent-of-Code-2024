with open("2015/data/2.txt", "r") as file:
    data = []
    for line in file:
        line.rstrip("\n")
        nums = [int(x) for x in line.split("x")]
        data.append(nums)

# print(data[0])

# part 1
def calcRequriedPaper(nums):
    l,w,h = nums
    sideAreas = [
        l*w,
        w*h,
        h*l
    ]
    surfaceArea = sum([x*2 for x in sideAreas])

    return surfaceArea + min(sideAreas)

# part 2
def calcRequriedRibbon(nums):
    l,w,h = nums
    vol = l*w*h
    nums = sorted(nums)
    shortSides = nums[:2]
    shortestPath = sum([x*2 for x in shortSides])

    return vol + shortestPath

total = 0
ribbonTotal = 0
for nums in data:
    total += calcRequriedPaper(nums)
    ribbonTotal += calcRequriedRibbon(nums)
    # break


print(total)
print(ribbonTotal)