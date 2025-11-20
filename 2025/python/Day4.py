import numpy as np

from utils import read_file

# Building the wordsearch, witha buffer for preventing indexing issues
def buffer(matrix, dex=3):
    dex = dex * 2
    y,x = matrix.shape
    big_array = np.array([['.' for x in range(x+dex)] for y in range(y+dex)])
    dex = dex // 2
    big_array[dex:-dex, dex:-dex] = matrix
    return big_array


# Part 1
# a function to grab all the possible correct answers for each postion
def look_around(word_search, row, col):
    grid = word_search
    matches = [
        # rows
        [grid[row][col], grid[row][col+1], grid[row][col+2], grid[row][col+3]],
        [grid[row][col], grid[row][col-1], grid[row][col-2], grid[row][col-3]],
        # diagonal
        [grid[row][col], grid[row+1][col+1], grid[row+2][col+2], grid[row+3][col+3]],
        [grid[row][col], grid[row-1][col-1], grid[row-2][col-2], grid[row-3][col-3]],
        [grid[row][col], grid[row-1][col+1], grid[row-2][col+2], grid[row-3][col+3]],
        [grid[row][col], grid[row+1][col-1], grid[row+2][col-2], grid[row+3][col-3]],
        # column
        [grid[row][col], grid[row+1][col], grid[row+2][col], grid[row+3][col]],
        [grid[row][col], grid[row-1][col], grid[row-2][col], grid[row-3][col]],
    ]
    return matches


# Part 2
def check_x(word_search, row, col):
    grid = word_search
    matches = [
        # diagonal
        [grid[row-1][col-1], grid[row][col], grid[row+1][col+1]],  # SE
        [grid[row+1][col+1], grid[row][col], grid[row-1][col-1]],  # NW
        [grid[row+1][col-1], grid[row][col], grid[row-1][col+1]],  # NE
        [grid[row-1][col+1], grid[row][col], grid[row+1][col-1]],  # SW
    ]
    return matches

#Da Loop
word_search = np.array([list(x) for x in read_file("input/day4.txt")])
word_search = buffer(word_search)
print(word_search)
xmasCount = 0
x_masCount = 0
for row in range(len(word_search)):
    for col in range(len(word_search[row])):
        if word_search[row][col] == "X":
            matches = look_around(word_search, row, col)
            xmasCount += len([match for match in matches if ''.join(match)=="XMAS"])
        if word_search[row][col] == "A":
            matches = check_x(word_search, row, col)
            if len([x for x in matches if ''.join(x) == "MAS"]) == 2:
                x_masCount +=1

print(xmasCount)
print(x_masCount)
