import re
import collections

# with open("test_input.txt", "r") as f:
# with open("test_input2.txt", "r") as f:
with open("input.txt", "r") as f:
    f = f.read().splitlines()


pad = lambda x: (x[0], x[1]) if len(x) >= 2 else (x[0], None)

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

buff = ""
def perform_op(t, op):
    global buff
    if buff == "": return t
    val = int(buff)
    buff = ""
    if op is None: return val
    return op(t, val)

def solve(s):
    t = 0
    op = None
    stack = []
    for l in s:
        if l == "(":
            stack.append((t, op))
            t = 0
            op = None
        elif l == ")":
            t = perform_op(t, op)
            t_t, op = stack.pop()
            if op is not None:
                t = op(t_t, t)
        elif l == " ":
            pass
        elif l == "+":
            t = perform_op(t, op)
            op = add 
        elif l == "*":
            t = perform_op(t, op)
            op = mul 
        else:
            global buff
            buff += l

    return perform_op(t, op)
        
print(sum([solve(l) for l in f]))
