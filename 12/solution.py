# with open("test_input.txt", "r") as f:
# with open("test_input2.txt", "r") as f:
with open("input.txt", "r") as f:
    f = f.read().splitlines()

directions = ["E", "S", "W", "N"]
instructions = list(map(lambda x: (x[0], int(x[1:])), f))

ship = 0 

pos = [0, 0]

for action, amount in instructions:
    if action == "R":
        ship += amount//90
        ship %= 4
        continue
    elif action == "L":
        ship -= amount//90
        ship %= 4
        continue

    if action == "F":
        action = directions[ship]

    if action == "E":
        pos[0] += amount
    elif action == "S":
        pos[1] -= amount
    elif action == "W":
        pos[0] -= amount
    elif action == "N":
        pos[1] += amount

print(abs(pos[0]) + abs(pos[1]))
