import re
import numpy as np

with open("input/day13.txt") as file:
    machine_data = file.read().split("\n\n")

test = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279""".split("\n\n")

# print(machine_data[0])

SHIFT = 10**13

class Machine():
    def __init__(self, data):
        self.breakout(data)
        self.a_count, self.b_count = self.line_mafs()
        self.total = self.total()
        
    def __repr__(self):
        return f"{self.a=}, {self.b=}, {self.prize=}"
    
    def breakout(self, data):
        lines = data.split("\n")
        self.a = tuple(int(x) for x in re.findall(r"(\d{1,})", lines[0]))
        self.b = tuple(int(x) for x in re.findall(r"(\d{1,})", lines[1]))
        # PART 1
        # self.prize = tuple(int(x) for x in re.findall(r"(\d{1,})", lines[2]))
        # PART 2
        self.prize = tuple(int(x)+SHIFT for x in re.findall(r"(\d{1,})", lines[2]))

    def det(self, a,b):
        return a[1] * b[0] - a[0] * b[1]

    def line_mafs(self):
        a_count = self.det(self.prize, self.b) / self.det(self.a, self.b)
        a_change = self.a[0] * a_count
        remaining = self.prize[0] - a_change
        b_count = remaining / self.b[0]

        return a_count, b_count
    
    def winnable(self):
        a = self.a_count
        b = self.b_count
        if a == int(a) and b== int(b):
            self.winnable = True
        else:
            self.winnable = False
        return self.winnable
    
    def total(self):
        if not self.winnable():
            # print("not winnable")
            return 0
        total = self.a_count * 3 + self.b_count
        return total

# machines = [Machine(data) for data in test]
machines = [Machine(data) for data in machine_data]
total= 0
for machine in machines:
    total+= machine.total

print(int(total))