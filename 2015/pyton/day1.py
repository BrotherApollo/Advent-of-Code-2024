with open("2015/data/1.txt", "r") as file:
    data = "".join([x for x in file])

# print(data)

# data = ")())())"

floor = 0
been_to_the_basement = False

for index, char in enumerate(data):
    if char == ")":
        floor -= 1
    if char == "(":
        floor += 1
    
    if floor == -1 and not been_to_the_basement:
        print(f"entered the basement at {index + 1}") # solution to part 2
        been_to_the_basement = True

print(floor) # solution to part 1