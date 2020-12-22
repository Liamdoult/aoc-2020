import re
import collections

# with open("test_input.txt", "r") as f:
# with open("test_input2.txt", "r") as f:
with open("input.txt", "r") as f:
    f = f.read().splitlines()



f = [[l if l in ["+", "*", "(", ")"] else int(l) for l in "".join(line.split(" "))] for line in f]

def brackets(l):
    stack = []
    current = []

    i = 0
    while i < len(l):
        if l[i] == "(":
            stack.append(current)
            current = []
        elif l[i] == ")":
            res = solve(current)
            current = stack.pop() + [res]
        else: current.append(l[i])
        i += 1

    return solve(current)


def solve(l):
    reduced = [l[0]]
    for i, v in enumerate(l):
        if v == "+":
            reduced[-1] = reduced[-1]+l[i+1]
        elif v == "*":
            reduced += [l[i+1]]

    t = 1
    for v in reduced:
        t *= v

    return t

print(sum([brackets(l) for l in f]))

