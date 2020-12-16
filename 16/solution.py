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


print(fields)
print(nearby)
error_rate = 0
for n in nearby:
    for v in n:
        print([(i, j, f"{fields[i][j][0]} <= {v} <= {fields[i][j][1]}", fields[i][j][0] <= v <= fields[i][j][1]) for i in range(len(fields)) for j in range(1, 3)])
        if not any([fields[i][j][0] <= v <= fields[i][j][1] for i in range(len(fields)) for j in range(1, 3)]):
            print(v)
            error_rate += v
print(error_rate)
