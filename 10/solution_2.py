import collections
import functools

# with open("test_input.txt", "r") as f:
# with open("test_input2.txt", "r") as f:
with open("input.txt", "r") as f:
    f = f.read().splitlines()

adapters = [0] + sorted(list(map(int, f)))

device = adapters[-1]+3
adapters.append(adapters[-1]+3)

differences = [0, 0, 0, 1]

lookup = collections.defaultdict(list) 
for i, a in enumerate(adapters):
    for j in range(a-3, a):
        lookup[j].append(i)

@functools.lru_cache
def get_permutations_count(i):
    v = adapters[i]
    if v == device: return 1

    t = 0
    for ai in lookup[v]:
        if ai != i:
            t += get_permutations_count(ai)
    return t

print(get_permutations_count(0))
