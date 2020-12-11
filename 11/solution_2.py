# with open("test_input.txt", "r") as f:
# with open("test_input2.txt", "r") as f:
with open("input.txt", "r") as f:
    f = f.read().splitlines()

seats = [[l for l in a] for a in f] 

seat_changed = True 

def print_seats(seats):
    for r in seats:
        print("".join(r))

def next_seat(r, c, ai, aj):
    i = r + ai
    j = c + aj
    while i >= 0 and j >= 0 and i < len(seats) and j < len(seats[0]):
        # print(r, c, i, j, ai, aj)
        if seats[i][j] == "#":
            return True
        elif seats[i][j] == "L":
            return False

        i += ai    
        j += aj

    return False

def count_neighbors(r, c):
    return sum([
        next_seat(r, c, 1, 0),
        next_seat(r, c, -1, 0),
        next_seat(r, c, 0, 1),
        next_seat(r, c, 0, -1),
        next_seat(r, c, 1, 1),
        next_seat(r, c, 1, -1),
        next_seat(r, c, -1, 1),
        next_seat(r, c, -1, -1),
    ])

# print_seats(seats)
while seat_changed is True:
    seat_changed = False
    next_state = [[""]*len(r) for r in seats]
    for r in range(len(seats)):
        for c in range(len(seats[0])):
            next_state[r][c] = seats[r][c]
            if seats[r][c] == ".":
                #print(r, c)
                continue
            n = count_neighbors(r, c)
            #print(r, c, n)
            if seats[r][c] == "L" and n == 0:
                next_state[r][c] = "#"
                seat_changed = True 
            if seats[r][c] == "#" and n > 4:
                next_state[r][c] = "L"
                seat_changed = True 
            # print(r, c, seats[r][c], next_state[r][c], n)
    
    #print(len(seats), len(seats[0]))
    seats = next_state
    #print("===========")
    #print_seats(seats)
    #exit()

t = 0
for r in seats:
    for c in r:
        if c == "#":
            t += 1

print(t)
