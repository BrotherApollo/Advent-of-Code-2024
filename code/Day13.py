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

SHIFT = 10000000000000

class Machine():
    def __init__(self, data):
        self.breakout(data)
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

    def snek_math(self):
        xdiff = (self.a[0], self.b[0])
        ydiff = (self.a[1], self.b[1])
        #local funciton for calculating determinat
        def det(a,b):
            return a[0] * b[1] - a[1] * b[0]
        
        div = det(xdiff, ydiff)
        if div == 0:
            print('lines dont intercsect homie')
        
        # Create lines using 2 known points
        a1 = self.prize
        a2 = (a1[0] - self.a[0], a1[1] - self.a[1])
        a_line = (a1, a2)

        b1 = self.b
        b2 = (0,0)
        b_line = (b1, b2)

        d = (det(*a_line), det(*b_line))
        x = det(d, xdiff)/div
        y = det(d, ydiff)/div
        
        self.intersect = (x,y)
        return x, y
    
    def winnable(self):
        x, y = self.snek_math()
        if x == int(x) and y== int(y):
            self.winnable = True
        else:
            self.winnable = False
        return self.winnable
    
    def total(self):
        if not self.winnable():
            print("not winnable")
            return 0
        b_presses = self.intersect[0] / self.b[0]
        a_presses = (self.prize[0] - self.intersect[0]) /self.a[0]
        totals = (a_presses * 3 + b_presses, a_presses + b_presses * 3)
        print(totals)
        print(f"{a_presses=}, {b_presses=}, {min(totals)=}")
        return min(totals)

# machines = [Machine(data) for data in test]
machines = [Machine(data) for data in machine_data]
total= 0
for machine in machines:
    total+= machine.total

print(int(total))

