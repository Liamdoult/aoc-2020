import functools

# with open("test_input.txt", "r") as f:
with open("input.txt", "r") as f:
    f = f.read().splitlines()

operations = list(map(lambda x: x.split(" "), f))

accumulator = 0
i = 0
visited = set()

while i not in visited:
    visited.add(i)
    op, val = operations[i]
    if op == "acc":
        accumulator += int(val)
        i += 1
    elif op == "nop": i += 1
    else: i += int(val)

print(accumulator)
