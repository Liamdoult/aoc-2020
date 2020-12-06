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

all_seats = []
for bp in f:
    row, seat = get_pos(bp[:7], 0, 127), get_pos(bp[7:], 0, 7, upper_tag="R")
    _id = row*8+seat
    all_seats.append((_id, row, seat, bp))

all_seats = sorted(all_seats, key=lambda x: x[0])

seats = set(map(lambda x: x[0], all_seats, ))
aval = set(range(all_seats[0][0], all_seats[-1][0]))

print(aval.difference(seats))
