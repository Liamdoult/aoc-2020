import functools

# with open("test_input.txt", "r") as f:
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
            bag = bag[2:]
            if bag[-1] == ".":
                bag = bag[:-1]
            if bag[-1] == "s":
                bag = bag[:-1]
            tmp.append(bag)
    graph[bag_type] = tmp

print(graph)

@functools.lru_cache
def has_bag(bag, looking_for="shiny gold bag"):   
    # if bag not in graph: return False
    sub_bags = graph[bag]
    if looking_for in sub_bags: return True
    for sub_bag in sub_bags:
        if has_bag(sub_bag, looking_for=looking_for): return True
    return False

results = [has_bag(key) for key in graph.keys()]

print(sum(results))


