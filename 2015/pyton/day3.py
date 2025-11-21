class Santa():
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, dir):
        if dir == "v":
            self.y += 1
        elif dir =="^":
            self.y -= 1
        elif dir == "<":
            self.x -= 1
        elif dir == ">":
            self.x += 1
        else:
            print("UNSUPPORTED MOVEMENT")

    def loc(self):
        return (self.x, self.y)
    

if __name__ == "__main__":
    with open("2015/data/3.txt", "r") as file:
        data = [x for x in file][0]
        # print(data)

    # data = "^>v<"

    # Part one
    santa = Santa()

    houses_visted = set()
    houses_visted.add(santa.loc())
    for dir in data:
        santa.move(dir)
        # print(santa.loc())
        houses_visted.add(santa.loc())

    print(f"Part one: Unique houses visited {len(houses_visted)}")

    # Part two
    santa = Santa()
    roboSanta = Santa()
    santasTurn = True

    houses_visted = set()
    # print(len(houses_visted))
    houses_visted.add(santa.loc())
    houses_visted.add(roboSanta.loc())

    for dir in data:
        if santasTurn:
            santa.move(dir)
            house = santa.loc()
        else:
            roboSanta.move(dir)
            house = roboSanta.loc()
        
        houses_visted.add(house)
        santasTurn = not santasTurn
        # print(santasTurn)

        # print(santa.loc(), roboSanta.loc())

    print(f"Part two: Unique houses visited {len(houses_visted)}")
        
    