
towels, designs = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb""".split("\n\n")
designs = designs.split("\n")
towels = [x.strip() for x in towels.split(",")]
print(towels)


test = designs[0]
print(f"goal: {test}")

towels_to_consider = []
for towel in towels:
    if towel in test:
        print(towel)
        towels_to_consider.append(towel)

print(towels_to_consider)