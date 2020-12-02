with open("input.txt", "r") as f:
    f = f.read().splitlines()

valid = 0
for r in f:
    pa, rest = r.split("-")
    pb, c, pw = rest.split(" ")

    pa = int(pa) - 1
    pb = int(pb) - 1
    c = c[0]

    if (c == pw[pa] or c == pw[pb]) and not (c == pw[pa] and c == pw[pb]):
        valid += 1

print(valid)


