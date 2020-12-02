with open("input.txt", "r") as f:
    f = f.read().splitlines()

f = map(int, f)
f = sorted(f)

print(f[:10])

for i in range(len(f)):
    for j in range(i, len(f)):
        for k in range(j, len(f)):
            if f[i] + f[j] + f[k] == 2020:
                print(f[i], f[j], f[k])
                print(f[i]*f[j]*f[k])
                exit()
            elif f[i] + f[j] + f[k] > 2020:
                continue
print("nothing found")
