import collections
import functools

# with open("test_input.txt", "r") as f:
# with open("test_input2.txt", "r") as f:
with open("input2.txt", "r") as f:
    f = f.read().splitlines()

trie = collections.defaultdict(list) 
images = []

before_break = True 
for l in f:
    if l == "":
        before_break = False 
        continue

    if before_break:
        l = "".join(l.split("\""))
        n, rules = l.split(":")
        rules = [a.strip().split(" ") for a in rules.split("|")]
        trie[n] = rules
    else:
        images.append(l)

# print(trie)
# print(images[:5])

def valid(image, rule="0", follow_on_rules=None):
    if len(image) == 0: return False
    for option in trie[rule]:
        if image[0] == option[0]:
            if follow_on_rules: return valid(image[1:], follow_on_rules[0], follow_on_rules[1:])
            if len(image) == 1: return True
            return False
        if valid(image, option[0], option[1:] + (follow_on_rules or [])): return True
    return False

valid_images = []
for image in images:
    if valid(image):
        print(image)
        valid_images.append(image)

print(len(valid_images))

