import math

data = open("input.txt").read().splitlines()
width = len(data[0])
height = len(data)
data = ''.join(data)
data = [int(x) for x in data]


def toPos(x, y):
    return y * width + x


def getAdjacent(index, data):

    x = index % width
    y = index // width
    adjacents = []

    if x != 0:
        adjacents.append(toPos(x - 1, y))
    if x != width - 1:
        adjacents.append(toPos(x + 1, y))
    if y != 0:
        adjacents.append(toPos(x, y - 1))
    if y != height - 1:
        adjacents.append(toPos(x, y + 1))

    return adjacents


def part1():
    s = 0
    for i in range(0, len(data)):
        adj = list(map(lambda x: data[x], getAdjacent(i, data)))
        if data[i] < min(adj):
            s += data[i] + 1
    return s


def getBasin(curr: list[int], index):
    val = data[index]
    if val == 9:
        return curr
    mas = list(filter(lambda x: data[x] != 9, getAdjacent(index, data)))
    #print("Search in:", mas, curr)
    for m in mas:
        if m not in curr:
            #print("Search add", m)
            curr += [m]
            b = getBasin(curr, m)
            curr += [x for x in b if x not in curr]
    return curr


def part2():
    basins = []
    for index in range(0, len(data)):
        #basins.add(getBasin([index], index))
        b = set(getBasin([index], index))
        if b not in basins and len(b) > 1:
            basins.append(b)
    basins = sorted(basins, key=len)
    return math.prod(map(len, basins[-3:]))


print(part1())
print(part2())
