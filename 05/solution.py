# with open("test_input.txt", "r") as f:
with open("input.txt", "r") as f:
    f = f.read().splitlines()

def get_pos(tree, upper, lower, upper_tag="B"):
    # print(tree, upper, lower)

    if len(tree) == 1:
        if tree == upper_tag: return lower 
        else: return upper 

    if tree[0] == upper_tag: 
        return get_pos(tree[1:], round((upper+lower)/2), lower, upper_tag)
    else: 
        return get_pos(tree[1:], upper, round((upper+lower)/2) - 1, upper_tag)

t = []
for bp in f:
    row, seat = get_pos(bp[:7], 0, 127), get_pos(bp[7:], 0, 7, upper_tag="R")
    _id = row*8+seat
    t.append(_id)

print("MAX: ", max(t))
