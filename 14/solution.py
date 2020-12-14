# with open("test_input.txt", "r") as f:
# with open("test_input2.txt", "r") as f:
with open("input.txt", "r") as f:
    f = f.read().splitlines()

memory_space = {}

def apply_mask(value, mask):
    if mask is None: return value

    one_mask, zero_mask = mask
    
    print("=====================+")
    print(value)
    print("{:b}".format(value), len("{:b}".format(value)), "value")
    value |= one_mask
    print("{:b}".format(one_mask), len("{:b}".format(one_mask)), "one_mask")
    print("{:b}".format(value), len("{:b}".format(value)), "value")
    value &= zero_mask
    print("{:b}".format(zero_mask), len("{:b}".format(zero_mask)), "zero_mask")
    print("{:b}".format(value), len("{:b}".format(value)), "value")
    print(value)
    print("=====================+")
    
    return value 

mask = None  
for l in f:
    if l[:2] == "ma":
        string_mask = l.split(" ")[-1]
        one_mask = 0b0
        not_mask = 0b0
        for d in string_mask:
            if d == "0":
                one_mask <<= 1
                not_mask <<= 1
                not_mask ^= 0
            elif d == "1":
                one_mask <<= 1
                not_mask <<= 1
                one_mask ^= 1
                not_mask ^= 1
            else:
                one_mask <<= 1
                not_mask <<= 1
                not_mask ^= 1

        mask = (one_mask, not_mask)
        print(f"{string_mask}\n", "{:b}\n".format(one_mask), "{:b}\n".format(not_mask))
    else:
        mem, _ , value = l.split(" ")
        mem = mem[4: -1]
        print(mem)
        value = int(value)
        memory_space[mem] = apply_mask(value, mask)

print(len("{:b}".format(sum(memory_space.values()))))

print(sum(memory_space.values()))
