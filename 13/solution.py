# with open("test_input.txt", "r") as f:
# with open("test_input2.txt", "r") as f:
with open("input.txt", "r") as f:
    f = f.read().splitlines()

arrive = int(f[0])
busses = list(map(int, [b for b in f[1].split(",") if b != "x"]))

res = sorted([(b-arrive%b, b) for b in busses], key=lambda b: b[0])
print(res)
print(res[0][0]*res[0][1])
