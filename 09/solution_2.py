# with open("test_input.txt", "r") as f:
with open("input.txt", "r") as f:
    f = f.read().splitlines()

lines = list(map(int, f))

# target = 127
target = 167829540

for i in range(len(lines)):
    j = i
    s = 0
    while s < target and j < len(lines):
        s += lines[j]
        if s == target and j - i > 1:
            print(i, j)
            mi = min(lines[i:j+1])
            ma = max(lines[i:j+1])
            print(mi, ma, mi+ma)
            exit() 
        j+= 1
