import functools

# with open("test_input.txt", "r") as f:
with open("input.txt", "r") as f:
    f = f.read().splitlines()

operations = list(map(lambda x: x.split(" "), f))

accumulator = 0
i = 0
visited = set()
back_track_i = -1
back_track_accumulator = 0
back_track_visited = visited.copy()

def do_op(op, val, i):
    if op == "acc":
        global accumulator
        accumulator += int(val)
        i += 1
    elif op == "nop": i += 1
    else: i += int(val)
    return i

while i != len(operations):
    if i in visited:
        i = back_track_i
        accumulator = back_track_accumulator
        visited = back_track_visited.copy()
        back_track_i = -1
        op, val = operations[i]
        visited.add(i)
        i = do_op(op, val, i)
    else:
        op, val = operations[i]
        visited.add(i)
        if back_track_i == -1 and (op == "jmp" or op == "nop"):
            back_track_accumulator = accumulator
            back_track_i = i
            back_track_visited = visited.copy()
            op = "nop" if op == "jmp" else "jmp" 
            i = do_op(op, val, i)
        else:
            i = do_op(op, val, i)
    
print(accumulator)
