f = open("input.txt").read()
f = f.splitlines()
a = int(f[0])
f.pop
count = 0
for nb in f:
    if (a < int(nb)):
        count += 1
    a = int(nb)
print(count)