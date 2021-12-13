f = open("input.txt").read()
f = f.splitlines()
h = 0
d = 0
a = 0
for line in f:
    if (line[0] == 'f') :
        h += int('0'+line[8])
        d += int('0'+line[8]) * a
    elif (line[0] == 'u'):
        a -= int('0'+line[3])
    else:
        a += int('0'+line[5])
print(h * d)
