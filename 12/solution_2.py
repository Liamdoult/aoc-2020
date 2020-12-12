# with open("test_input.txt", "r") as f:
# with open("test_input2.txt", "r") as f:
with open("input.txt", "r") as f:
    f = f.read().splitlines()

directions = [
    lambda x: [y, -x],  # E -> S
    lambda x: [y, -x],  # S -> W 
    lambda x: [y, abs(x)],  # W -> N 
    lambda x: [y, abs(x)],  # N -> E 
]

def rotate(x, y):
    if x < 0:
        return y, abs(x)
    return [y, -x]

def nrotate(x, y, n=1):
    for _ in range(n):
        x, y = rotate(x, y)
    return [x, y]

instructions = list(map(lambda x: (x[0], int(x[1:])), f))


waypoint = [10, 1]
ship = [0, 0]

for action, amount in instructions:
    if action == "R":
        waypoint = nrotate(*waypoint, n=amount//90%4)
        continue
    elif action == "L":
        waypoint = nrotate(*waypoint, n=4-(amount//90%4))
        continue

    if action == "F":
        ship[0] += amount * waypoint[0]
        ship[1] += amount * waypoint[1]
    elif action == "E":
        waypoint[0] += amount
    elif action == "S":
        waypoint[1] -= amount
    elif action == "W":
        waypoint[0] -= amount
    elif action == "N":
        waypoint[1] += amount

print(abs(ship[0]) + abs(ship[1]))
