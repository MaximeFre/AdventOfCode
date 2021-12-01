f = open("input.txt").read()
f = f.splitlines()
a = int(f[0]) + int(f[1]) + int(f[2])
x = 1
count = 0
while x < (f.__len__() - 2):
    y = int(f[x]) + int(f[x + 1]) + int(f[x + 2])
    if (a < y):
        count += 1
    a = y
    x += 1
print(count)