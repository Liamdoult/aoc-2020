import functools

# with open("test_input2.txt", "r") as f:
with open("input.txt", "r") as f:
    f = f.read().splitlines()

# build graph
graph = {} 
for line in f:
    bag_type, sub_types = line.split(" contain ")

    bag_type = bag_type.strip()
    if bag_type[-1] == "s":
        bag_type = bag_type[:-1]

    tmp = []
    if sub_types != "no other bags.":
        for bag in sub_types.split(","):
            bag = bag.strip()
            count, bag = bag.split(" ", 1)
            count = int(count)
            if bag[-1] == ".":
                bag = bag[:-1]
            if bag[-1] == "s":
                bag = bag[:-1]
            tmp.append((count, bag))
    graph[bag_type] = tmp

print(graph)

@functools.lru_cache
def count(bag):
    # if bag not in graph: return False
    sub_bags = graph[bag]
    t = 1
    for c, sub_bag in sub_bags:
        print(c, sub_bag)
        t += c * count(sub_bag)
    return t

print(count("shiny gold bag")-1)


