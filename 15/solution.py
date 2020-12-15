# with open("test_input.txt", "r") as f:
# with open("test_input2.txt", "r") as f:
with open("input.txt", "r") as f:
    f = f.read().splitlines()

target = 30000000
start = list(map(int, f[0].split(",")))

last = {v: i+1 for i, v in enumerate(start)}

current = 0

for i in range(len(start)):
    print(i, start[i])

for i in range(len(start)+1, target):
    # print(i, current)
    if current in last:
        new_current = i - last[current]
        last[current] = i
        current = new_current
    else:
        last[current] = i
        current = 0

print(current)

