# with open("test_input.txt", "r") as f:
with open("input.txt", "r") as f:
    f = f.read().splitlines()

t = 0
answers =  set()
for line in f:
    if line == "":
        t += len(answers)
        answers = set()
    else:
        for l in line:
            answers.add(l)

t+=len(answers)
print(t)

