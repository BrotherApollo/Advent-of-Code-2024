from utils import read_file
from copy import deepcopy

class Depresser(object):
    def __init__(self, rawdata):
        self.rawdata = rawdata
        print("starting the data breakout")
        self.data = self.flatten_lists(self.break_out())
        print("finished breakout, starting compression")
        self.compress()
        print("generating checksum")
        self.chekcsum = self.total()

    def break_out(self):
        que = deepcopy(self.rawdata)
        index = 0
        output = []
        empty = False
        while que:
            if empty:
                empty = que.pop(0)
                output.append(["." for x in range(int(empty))])
                # print(f"{index=}, {empty=}")
                # print(output)
            else:
                data = que.pop(0)
                output.append([index for x in range(int(data))])
                index +=1
                # print(f"{index=}, {data=}")
                # print(output)
            empty = not empty
        return output
    
    def flatten_lists(self, data):
        output = []
        for lst in data:
            output+= lst
        return output

    def get_byte(self, index):
        # print(self.data[:index:-1])
        for index, item in enumerate(self.data[:index:-1]):
            if item != ".":
                reverse_index = (index +1) *-1
                # print(index, item, reverse_index)
                self.data.pop(reverse_index)
                self.data.insert(reverse_index, ".")
                return item

    def compress(self):
        for index, item in enumerate(self.data):
            if item == ".":
                # print(f"{index=}")
                byte = self.get_byte(index)
                # print(byte)
                if byte:
                    self.data.pop(index)
                    self.data.insert(index, byte)
    
    def total(self):
        total = 0
        for index, item in enumerate(self.data):
            if item != ".":
                product = index * int(item)
                total += product
        return total


# Main
# data = list("2333133121414131402")
# print(data)
"00...111...2...333.44.5555.6666.777.888899"

lines = read_file("input/day9.txt")
data = list(lines[0])
# print(data)

depress = Depresser(data)

# # print(depress.data)
print(depress.chekcsum)