# with open("test_input.txt", "r") as f:
with open("input.txt", "r") as f:
    f = f.read().splitlines()

lines = list(map(int, f))

preamble = 25

i = preamble - 1

while i < len(lines):
    i += 1
    look = set(lines[i-preamble:i])
    for v in lines[i-preamble:i]:
        if lines[i] - v in look:
           break 
    else:
        print(lines[i])
        exit()
            
print("Nothing found")
