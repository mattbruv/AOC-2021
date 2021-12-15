data = open("input.txt").read().splitlines()
width = len(data[0])
height = len(data)
data = ''.join(data)
data = [int(x) for x in data]

tot = width * height
print(width, "x", height)


def toPos(x, y):
    return y * width + x


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


adjacentLookup = {}

for i in range(0, len(data)):
    adjacentLookup[i] = getAdjacent(i, offsetsPart1)
print("Populated adjacent lookup table")


def pathValue(path):
    ans = sum([data[x] for x in path])
    return ans


testPaths = [
    # left -> right -> down
    list(range(0, width - 1)) + list(range(width - 1, len(data), width)),

    # left -> right diagonally
    # list(range(0, len(data), width + 1)),

    # left -> down -> right
    list(range(0, len(data), 10)) +
    list(range(width * height - width + 1, len(data)))
]

testValues = list(map(pathValue, testPaths))
minimumStart = min(testValues)

minimum = minimumStart


def search(index, accumulator):
    global minimum
    adjacents = adjacentLookup[index]

    if len(adjacents) == 0:
        # TODO
        if accumulator < minimum:
            minimum = accumulator
        return

    for choice in adjacents:
        value = data[choice]
        nextSum = accumulator + value
        print(nextSum, minimum)
        # Do not search down more expensive paths
        if nextSum > minimum:
            continue
        # search the next path
        search(choice, nextSum)


search(0, 0)
print(minimum)
