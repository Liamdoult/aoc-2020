# with open("test_input.txt", "r") as f:
with open("input.txt", "r") as f:
    f = f.read().splitlines()

m = [list(map(lambda x: True if x == "#" else False, r)) for r in f]

pos = []
for i, v in enumerate(m[1:]):
    p = ((i+1)*3) % len(v)
    pos.append(v[p])

print(sum(pos))


