# with open("test_input.txt", "r") as f:
# with open("test_input2.txt", "r") as f:
with open("input.txt", "r") as f:
    f = f.read().splitlines()

seats = [[l for l in a] for a in f] 

seat_changed = True 

def print_seats(seats):
    for r in seats:
        print("".join(r))

def count_neighbors(r, c):
    n = 0
    t = 0
    for i in range(max(0, r-1), min(len(seats)-1, r+1)+1):
        for j in range(max(0, c-1), min(len(seats[i])-1, c+1)+1):
            if i != r or j != c:
                if seats[i][j] == "#":
                    n+=1
                t += 1
            # if r == 1 and c == 3:
                # print(r, c, i, j, seats[i][j], n)
    return n, t

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
            n, t = count_neighbors(r, c)
            #print(r, c, n, t)
            if seats[r][c] == "L" and n == 0:
                next_state[r][c] = "#"
                seat_changed = True 
            if seats[r][c] == "#" and n > 3:
                next_state[r][c] = "L"
                seat_changed = True 
            # print(r, c, seats[r][c], next_state[r][c], n)
    
    #print(len(seats), len(seats[0]))
    seats = next_state
#    print("===========")
#    print_seats(seats)

t = 0
for r in seats:
    for c in r:
        if c == "#":
            t += 1

print(t)
