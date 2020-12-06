import collections

# with open("test_input.txt", "r") as f:
with open("input.txt", "r") as f:
    f = f.read().splitlines()

t = 0
answers = collections.defaultdict(int) 
n = 0
for line in f:
    if line == "":
        for key, value in answers.items():
            if value == n:
                t += 1
        n = 0
        answers = collections.defaultdict(int) 
    else:
        n += 1
        for l in line:
            answers[l] += 1

for key, value in answers.items():
    if value == n:
        t += 1
print(t)

