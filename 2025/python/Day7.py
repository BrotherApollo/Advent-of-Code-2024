from utils import read_file
from copy import deepcopy
import itertools

test = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".split("\n")

def math(values, operations):
    output = values[0]
    for i in range(len(values)-1):
        num = values[i+1]
        method = operations[i]
        if method == "+":
            output += num
        elif method == "*":
            output *= num
        else:
            temp = str(output) + str(num)
            output = int(temp)
    return output

data = read_file("input/day7.txt")
total = 0
for line in data:
# line = "46217848: 17 3 4 9 2 9 74 4 46 2 7 3"
    data = [x.strip() for x in line.split(":")]
    answer = int(data[0])
    values = [int(x) for x in data[1].split()]
            
    print(total)
    x = [["+", "*", '||'] for x in range(len(values)-1)]
    print(x)
    options = [element for element in itertools.product(*x)]
    print(len(options))
    for option in options:
        if math(values, operations=option) == answer:
            print('yert')
            total+= answer
            break
print(total)
    