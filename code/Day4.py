import numpy as np

from utils import read_file

test= """
XMAS
SAMS
SAAA
SMMM
XXXX
""".split("\n")

# Building the wordsearch, witha buffer for preventing indexing issues
test = [list(f"....{x}....") for x in test if x]
data = [list(f"...{x}....") for x in read_file("input/day4.txt")]
buffer = [['.' for x in range(len(data[0]))]for x in range(4)]
word_search = np.array(buffer+data+buffer)
print(word_search)

    

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
        [grid[row][col], grid[row-1][col-1], grid[row+2][col-2], grid[row+3][col-3]],
        # column
        [grid[row][col], grid[row+1][col], grid[row+2][col], grid[row+3][col]],
        [grid[row][col], grid[row-1][col], grid[row-2][col], grid[row-3][col]],
    ]
    return matches

count = 0
for row in range(len(word_search)):
    for col in range(len(word_search[row])):
        if word_search[row][col] != "X":
            continue
        matches = look_around(word_search, row, col)
        count += len([match for match in matches if ''.join(match)=="XMAS"])

print(count)


#attempt 2

# valid_words = ["XMAS", "SAMX"]

# def check(words:list[str], matrix:np.array, x:int, y:int, dX:int, dY:int, word_index:int=0) -> bool:
#     if y < 0 or y >= len(matrix) or x < 0 or x >= len(matrix[y]):
#         return False
        
#     words = [word for word in valid_words if word[word_index] == word_search[y][x]]
#     if not words:
#         return False
#     if word_index == max([len(word) for word in words])-1:
#         return True
#     else:
#         return check(
#             words=words,
#             matrix=word_search,
#             x=x + dX,
#             y=x + dY,
#             dX=dX,
#             dY=dY,
#             word_index=word_index + 1
#         )

# wordCount = 0
# for y in range(len(word_search)):
#     for x in range(len(word_search[y])):
#         wordCount += sum(1 for find in [
#                 check(valid_words, word_search, x, y, 1, 0),
#                 check(valid_words, word_search, x, y, 1, 1),
#                 check(valid_words, word_search, x, y, 0, 1),
#                 check(valid_words, word_search, x, y, -1, 1)
#             ] if find)

# print(wordCount)