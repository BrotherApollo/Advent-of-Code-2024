from utils import read_file

test = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn""".split("\n")

data = read_file("input/day23.txt")
mapping = {}

for line in test:
    a, b = line.split('-')
    # print(a,b)
    if mapping.get(a):
        mapping[a].append(b)
    else:
        mapping[a] = [b]
    
    if mapping.get(b):
        mapping[b].append(a)
    else:
        mapping[b] = [a]
        
# print(mapping)
 ## Part 1
cliques = []
for parent in mapping.keys():
    if not parent.startswith('t'):
        continue
    clique = [x for x in mapping.get(parent)]
    for child in mapping.get(parent):
        for grand in mapping.get(child):
            if parent in mapping.get(grand):
                # print(parent, child, grand)
                cliques.append((parent, child, grand))

def dedup(items):
    output = []
    for line in items:
        dupe = False
        for result in output:
            bool_bag = [x in result for x in line]
            if all(bool_bag):
                dupe = True
                break
        if dupe:continue
        output.append(line)
    return output

print(len(cliques))
deduped = dedup(cliques)
print(len(deduped))

# for i in deduped:
#     print(i)
        
## Part 2
from networkx.algorithms import approximation
import networkx as nx
g = nx.Graph()
for line in data:
    a,b = line.split("-")
    g.add_edge(a,b)
max_clique = approximation.max_clique(g)
print(max_clique)

print(",".join(sorted(max_clique)))