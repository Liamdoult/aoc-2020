with open("input.txt", "r") as f:
    f = f.read().splitlines()

valid = 0
for r in f:
    min_c, rest = r.split("-")
    max_c, c, pw = rest.split(" ")

    min_c = int(min_c)
    max_c = int(max_c)
    c = c[0]


    t = 0
    for l in pw:
        if c == l:
            t += 1
    
    if t <= max_c and t >= min_c:
        valid += 1

    print(min_c, max_c, c, pw, t)

print(valid)


