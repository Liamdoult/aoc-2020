import collections

# with open("test_input.txt", "r") as f:
# with open("test_input2.txt", "r") as f:
with open("input.txt", "r") as f:
    f = f.read().splitlines()

fields, ticket, nearby = [], [], []

section = 0
for l in f:
    if l == "":
        section += 1
        continue
    if section == 0:
        field_name, ranges = l.split(":")
        range_a, range_b = ranges.strip().split(" or ")
        range_a = list(map(int, range_a.split("-")))
        range_b = list(map(int, range_b.split("-")))
        fields.append((field_name, range_a, range_b))
    elif section == 1:
        if l != "your ticket:":
            ticket = list(map(int, l.split(",")))
    elif section == 2:
        if l != "nearby tickets:":
            nearby.append(list(map(int, l.split(","))))


valid_nearby = []
for n in nearby:
    if all([any([fields[i][j][0] <= v <= fields[i][j][1] for i in range(len(fields)) for j in range(1, 3)]) for v in n]):
        valid_nearby.append(n)


field_col = collections.defaultdict(list) 
for field in fields:
    for j in range(len(valid_nearby[0])):
        if all([(field[1][0] <= valid_nearby[i][j] <= field[1][1]) or (field[2][0] <= valid_nearby[i][j] <= field[2][1]) for i in range(len(valid_nearby))]):
            field_col[j].append(field[0])

print(field_col)

cols = {}
for k, v in sorted(field_col.items(), key=lambda x: len(x[1])):
    if len(v) == 1:
        cols[v[0]] = k
        continue
    for p in v:
        if p not in cols:
            cols[p] = k
            break

print(cols)
assert len(cols) == len(fields)

t = 1
for k, v in cols.items():
    if "departure" in k:
        t *= ticket[v]
print(t)
