from utils import read_file

data = read_file("input/day5.txt")
# data = """47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47""".split("\n")


def parse_data(data):
    rules = []
    pages = []
    switch = False
    for line in data:
        if line == "":
            switch = True
            continue
        if switch:
            pages.append(line)
        else:
            rules.append(line)
    return (rules, pages)

rules, pages = parse_data(data)
pages = [x.split(",") for x in pages]

def bad_prequel(page, rules):
        # filters rules list to pages that can no come before current page
        return [x.split("|")[1] for x in rules if page == x.split("|")[0]]
    
def check(rules:list[str], page_set:list[str]) -> bool:
    for index, curr_page in enumerate(page_set):
        bad_prequels = bad_prequel(page=curr_page, rules=rules)
        # print(curr_page, incorret_if_before)
        for page in bad_prequels:
            if page in page_set[:index]:
                return False
    return True

def reorder(rules, page_set):
    step = 0
    while check(rules=rules, page_set=page_set) == False:
        step +=1 
        if step > 100:
            print("hit max step")
            break
        for index, curr_page in enumerate(page_set):
            bad_prequels = bad_prequel(page=curr_page, rules=rules)
            for page in bad_prequels:
                if page in page_set[:index]:
                    # print(page_set)
                    old_index = page_set.index(page)
                    page_set.pop(old_index)
                    page_set.insert(index, page)
                    # print(page_set)
    return page_set        
    

Part1_total = 0
wrong_sets = []
for page_set in pages:
    x = check(rules=rules, page_set=page_set)
    # print(x)
    if x:
        mid_index = len(page_set)//2
        Part1_total += int(page_set[mid_index])
    else:
        wrong_sets.append(page_set)
        
print(Part1_total)
corrected_pages = [reorder(rules=rules, page_set=x) for x in wrong_sets]

Part2_total = 0
for page_set in corrected_pages:
    mid_index = len(page_set)//2
    Part2_total += int(page_set[mid_index])
    
print(Part2_total)
# for x,y in zip(wrong_sets, corrected_pages):
#     print(x,"\n", y)