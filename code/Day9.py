from utils import read_file
from copy import deepcopy

class Depresser(object):
    def __init__(self, rawdata):
        self.rawdata = rawdata
        print("starting the data breakout")
        self.data = self.break_out()
        print("finished breakout, starting compression")
        # Part 1
        # self.data = self.flatten_lists(self.data)
        # self.compress() 

        # Part 2
        self.part2_compress()
        # print(self.data)
        self.data = self.flatten_lists(self.data)
        
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
            else:
                data = que.pop(0)
                output.append([index for x in range(int(data))])
                index +=1
            empty = not empty
        return output
    
    def find_location(self, data_set, curr_index):
        # print(self.data)
        for index, item in enumerate(self.data):
            if index > curr_index:
                break
            if "." in item:
                if len(item) >= len(data_set):
                    return index

    def part2_compress(self):
        for reverse_index, item in enumerate(self.data[::-1]):
            curr_index = self.data.index(item)

            if "." not in item:
                new_index = self.find_location(data_set=item, curr_index=curr_index)
                if not new_index:
                    continue
                old_data = self.data[new_index]
                size_diff = len(old_data) - len(item)
                self.data[curr_index] = ["." for x in item]
                self.data[new_index] = item
                # print(f"{size_diff=}, {old_data}, {item}")
                if size_diff:
                    self.data.insert(new_index+1, ["." for x in range(size_diff)])
    
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
lines = read_file("input/day9.txt")
data = list(lines[0])
# data = list("2333133121414131402")
# print(data)

depress = Depresser(data)

# print(depress.data)
print(depress.chekcsum)