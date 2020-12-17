import collections

# with open("test_input.txt", "r") as f:
# with open("test_input2.txt", "r") as f:
with open("input.txt", "r") as f:
    f = f.read().splitlines()

print(f)

cycles = 6

positions = []

yzr = len(f)//2
xzr = len(f[0])//2

for i in range(len(f)):
    for j in range(len(f[i])):
        if f[i][j] == "#":
            positions.append((j-xzr, i-yzr, 0, 0))


print(positions)


for _ in range(cycles):

    new_pos_map = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(int)))) 
    active = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(bool)))) 

    for p in positions:
        for w in range(-1, 2):
            for z in range(-1, 2):
                for y in range(-1, 2):
                    for x in range(-1, 2):
                        _x, _y, _z, _w = p
                        if (x, y, z, w) == (0, 0, 0, 0):
                            active[_x+x][_y+y][_z+z][_w+w] = True
                        else:
                            new_pos_map[_x+x][_y+y][_z+z][_w+w] += 1

    positions = []
    for x, xd in new_pos_map.items(): 
        for y, yd in xd.items(): 
            for z, zd in yd.items(): 
                for w, v in zd.items(): 
                    if active[x][y][z][w] and 3 >= v >= 2:
                        positions.append((x, y, z, w))
                    elif not active[x][y][z][w] and v == 3:
                        positions.append((x, y, z, w))

print(positions)
print(len(positions))
