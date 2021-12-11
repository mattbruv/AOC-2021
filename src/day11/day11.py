data = open("input.txt").read().splitlines()
data = open("test.txt").read().splitlines()
width = len(data[0])
height = len(data)
data = ''.join(data)
data = [int(x) for x in data]


def toPos(x, y):
    return y * width + x


def toPoint(index):
    x = index % width
    y = index // height
    return (x, y)


# returns a list ofadjacent indexes
offsets = [-1, 1, -width, width,
           (-width - 1), (-width + 1), (width - 1), (width + 1)]

tot = width * height


def isValidIndex(originalIndex, newIndex):
    o = originalIndex
    n = newIndex
    if not (n >= 0 and n < width * height):
        return False
    p1 = toPoint(o)
    p2 = toPoint(n)
    if p2[0] < 0 or p2[1] < 0:
        return False
    if p2[0] > tot or p2[1] > tot:
        return False
    if (abs(p2[0]) - abs(p1[0]) > 1) or (abs(p1[0]) - abs(p2[0]) > 1):
        return False
    if (abs(p2[1]) - abs(p1[1]) > 1) or (abs(p1[1]) - abs(p2[1]) > 1):
        return False
    return True


def getAdjacent(index):

    x = index % width
    y = index // width
    adjacents = list(map(lambda x: x + index, offsets))
    adj = list(filter(lambda x: isValidIndex(index, x), adjacents))

    return sorted(adj)


def getFlashers(data) -> set:
    fs = set()
    for i in range(0, len(data)):
        if data[i] > 9:
            fs.add(i)
    return fs


def flash(data):
    flashCount = 0
    flashIndexes = set()
    while True:
        toFlash = getFlashers(data).difference(flashIndexes)
        flashIndexes = flashIndexes.union(toFlash)
        flashCount += len(toFlash)
        if len(toFlash) == 0:
            break
        #print("Flash:", toFlash)
        # apply each flash
        for f in toFlash:
            data[f] = 0
            adj = getAdjacent(f)
            for a in adj:
                #print(a, f)
                data[a] += 1
    for f in flashIndexes:
        data[f] = 0

    return (data, flashCount)


def step(data):
    newData = list(map(lambda x: x + 1, data))
    d = flash(newData)
    return d


flashes = 0

for i in range(0, 100):
    data, fs = step(data)
    flashes += fs
    #print(data, fs)

print(flashes)


i = 0
while True:
    i += 1
    data, fs = step(data)
    if i == 1:
        break


def p(data):
    n = 0
    for i in range(0, len(data)):
        x = toPoint(i)
        print(x)


p(data)
# if len(list(filter(lambda x: x == 0, data))) == 100:
# print(data, i)
#    break
