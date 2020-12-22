import collections
import functools

# with open("test_input.txt", "r") as f:
# with open("test_input2.txt", "r") as f:
with open("input.txt", "r") as f:
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

@functools.lru_cache
def generate(rule="0"):
    if rule not in trie: return set(rule)
    all_options = []
    for option in trie[str(rule)]:
        current_options = generate(rule=option[0])
        for r in option[1:]:
            current_options = [curr+other for curr in current_options for other in generate(rule=r)]
        all_options += current_options
    return set(all_options)
lookup = generate()

valid_images = []
for image in images:
    if image in lookup:
        valid_images.append(image)

print(len(valid_images))





