# with open("test_input.txt", "r") as f:
with open("input.txt", "r") as f:
    f = f.read().splitlines()

m = [list(map(lambda x: True if x == "#" else False, r)) for r in f]

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

t = 1
for r, d in slopes:
    pos = []
    # print("slope: ", r, d)
    for i in range(d, len(m), d):
        p = ((i//d)*r) % len(m[0])
        # print(i, p, m[i][p])
        pos.append(m[i][p])

    print((r, d), sum(pos))
    t *= sum(pos)

print(t)
