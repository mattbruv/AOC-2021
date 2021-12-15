data = open("test.txt").read().splitlines()
width = len(data[0])
height = len(data)
data = ''.join(data)
data = [int(x) for x in data]

tot = width * height
print(width, "x", height)


def toPoint(index):
    x = index % width
    y = index // height
    return (x, y)


# returns a list ofadjacent indexes
offsetsPart1 = [1, width]
#offsetsPart1 = [-1, 1, -width, width]
# (-width - 1), (-width + 1), (width - 1), (width + 1)]


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


def getAdjacent(index, offsets):

    x = index % width
    y = index // width
    adjacents = list(map(lambda x: x + index, offsets))
    adj = list(filter(lambda x: isValidIndex(index, x), adjacents))

    return sorted(adj)


floodMap = [float("inf") for x in data]
floodMap[0] = data[0]

scanList = [0]


def scan(scanList):
    newList = []
    for index in scanList:
        neighbors = getAdjacent(index, offsetsPart1)
        for n in neighbors:
            data[n] += data[index]
            floodVal = floodMap[n]
            if data[n] < floodVal:
                floodMap[n] = data[n]
                newList.append(n)
    return newList


while len(scanList) > 0:
    scanList = scan(scanList)


"""
Go over a "scan list" of points to update.
The value at the flood cell is added
to the value of each of its neighbours cells
in the "risk" grid.

If the value of a neighbour is smaller than
the equivalent cell in the flood map,
that cell is updated and the cell point is added
to a new scanlist.
"""
