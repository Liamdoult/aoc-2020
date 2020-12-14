from dataclasses import dataclass
import fileinput
from functools import reduce
from itertools import chain, product

# with open("test_input.txt", "r") as f:
# with open("test_input2.txt", "r") as f:
with open("input.txt", "r") as f:
    f = f.read().splitlines()

@dataclass
class Mask:
    off: int
    on: int

@dataclass
class Write:
    addr: int
    value: int


def parse(line):
    if line.startswith('mask = '):
        mask = line[7:]
        return Mask(off=int(mask.replace('X', '0'), base=2),
                    on=int(mask.replace('X', '1'), base=2))
    if line.startswith('mem['):
        i = line.index('] = ')
        return Write(addr=int(line[4:i]), value=int(line[i + 4:]))

def part2(lines):
    mem = {}
    for line in lines:
        instruction = parse(line)
        if isinstance(instruction, Mask):
            maskoff, maskon = instruction.off, instruction.on
        elif isinstance(instruction, Write):
            diff = maskoff ^ maskon
            popcount = bin(diff).count('1')
            for i in range(1 << popcount):

                def f(acc, j):
                    x, k = acc
                    return (x ^ diff & (k ^ k - (i >> j & 1)), k & k - 1)

                mem[reduce(
                    f, range(popcount),
                    (instruction.addr | maskoff, diff))[0]] = instruction.value
    return sum(mem.values())

print(part2(f))
