# with open("test_input.txt", "r") as f:
# with open("test_input2.txt", "r") as f:
with open("input.txt", "r") as f:
    f = f.read().splitlines()

adapters = sorted(list(map(int, f)))

differences = [0, 0, 0, 1]

jolts = 0
for adapter in adapters:
    differences[adapter-jolts] += 1
    jolts = adapter

print(differences)
print(differences[1] * differences[3])
