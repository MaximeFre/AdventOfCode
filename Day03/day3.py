f = open("input.txt").read()
f = f.splitlines()
a = 0
b = 0
g = ""
e = ""
for i in range(len(f[0])):
    a = 0
    b = 0
    for lines in f:
        if (lines[i] == '0'):
            a += 1
        else:
            b += 1
    if (a > b):
        g += '0'
        e += '1'
    else:
        e += '0'
        g += '1'
g = int(g, 2)
e = int(e, 2)
print(g * e)
        
