# with open("test_input.txt", "r") as f:
# with open("test_input2.txt", "r") as f:
with open("input.txt", "r") as f:
    f = f.read().splitlines()

busses = [(int(b), i) for i, b in enumerate(f[1].split(",")) if b != "x"]

jump = i = busses[0][0] 
for b in busses[1:]:
    while (i+b[1])%b[0] != 0:
        i += jump
    jump *= b[0]

print(i)

