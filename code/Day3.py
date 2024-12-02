# Standard Import
import re





with open("input/day3.txt", "r") as file:
    data = file.read()

results = re.findall(r"([mul]{2,3}\([\d]{1,5},[\d]{1,5}\)|[don't]{2,5}\(\))", data)
# print(results)
total = 0
# for thing in results:
#     if "mul" not in thing:
#         print(thing)
execute = True
for func in results:
    func.strip("' ")
    if "do()" in func:
        execute = True
    elif "don't()" in func:
        execute = False
    elif 'mul' in func:
        if execute:
            a,b = func.strip("mul()").split(',')
            temp = int(a) * int(b)
            total += temp
    else:
        print(f'something went wrong, {func}')
print(total)