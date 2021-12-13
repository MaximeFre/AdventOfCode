def checkGood(bingo):
    for y in range(len(bingo)):
        resX = 0
        resY = 0
        for x in range(len(bingo)):
            if (bingo[y][x] != 'x'):
                resX = 1
            if (bingo[x][y] != 'x'):
                resY = 1
        if (resX == 0 or resY == 0):
            return 1
    return 0

def getTotal(tab, nb):
    sum = 0
    for y in range(len(tab)):
        for x in range(len(tab)):
            if (tab[y][x] != 'x'):
                sum += int(tab[y][x])
    return sum * nb

def getGame():
    f = open("input.txt").read()
    f = f.splitlines()
    game = f[0].split(',')
    return game

def parseBingo():
    f = open("input.txt").read()
    f = f.splitlines()
    f.pop(0)
    f.pop(0)
    tab = []
    temp = []
    for lines in f:
        if (lines == ""):
            tab.append(temp)
            temp = []
        else:
            temp.append(lines.split())
    return tab

def putX(nb, tab):
    for bingo in tab:
        for y in range(len(bingo)):
            for x in range(len(bingo)):
                if (bingo[y][x] == nb):
                    bingo[y][x] = 'x'
    return tab

def main():
    tab = parseBingo()
    numbers = getGame()
    lastNb = 0
    for nb in numbers:
        lastNb = nb
        tab = putX(nb, tab)
        for bingo in tab:
            if (checkGood(bingo) == 1 and len(tab) != 1):
                tab.remove(bingo)
            if (len(tab) == 1 and checkGood(tab[0]) == 1):
                break
        if (len(tab) == 1 and checkGood(tab[0]) == 1):
            break
    print(getTotal(tab[0], int(lastNb)))
    

if __name__ == "__main__":
    main()