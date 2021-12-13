f = open("input.txt").read()
f = f.splitlines()
a = 0
b = 0
g = f
e = f
i = 0

while (len(g) != 1):
    a = 0
    b = 0
    for lines in g:
        if (lines[i] == '0'):
            a += 1
        else:
            b += 1
    if (a > b):
        g = [x for x in g if x[i] == '1']
        # for idx, lines in enumerate(g):
        #     if (lines[i] == '1'):
        #         del g[idx]
    else:
        g = [x for x in g if x[i] == '0']
        # for idx, lines in enumerate(g):
        #     if (lines[i] == '0'):
        #         del g[idx]
    i += 1
print(g)
i = 0
while (len(e) != 1):
    a = 0
    b = 0
    for lines in e:
        if (lines[i] == '0'):
            a += 1
        else:
            b += 1
    if (a > b):
        e = [x for x in e if x[i] == '0']
        # for idx, lines in enumerate(e):
        #     if (lines[i] == '0'):
        #         del e[idx]
    else:
        e = [x for x in e if x[i] == '1']
        # for idx, lines in enumerate(e):
        #     if (lines[i] == '1'):
        #         del e[idx]
    i += 1
print(e)
d = int(g[0], 2)
p = int(e[0], 2)
print(d * p)
        
