import time

# BEWARE
# THIS IS THE MOST DISGUSTING CODE I"VE WRITTEN IN PROBABLY HALF A DECADE
# VERY SLOW TOO BUT IT DOES THE JOB


def parsePoints(points):
    p1s = points[0].split(",")
    p2s = points[1].split(",")
    return [(int(p1s[0]), int(p1s[1])), (int(p2s[0]), int(p2s[1]))]


data = open("input.txt").read().splitlines()
#data = open("test.txt").read().splitlines()
data = list(map(lambda x: x.split(" -> "), data))
data = list(map(parsePoints, data))


def vecPoints(vector):
    p1, p2 = vector
    line = []

    if p1[0] == p2[0]:
        minimum = min([p1[1], p2[1]])
        maximum = max([p1[1], p2[1]])
        for y in range(minimum, maximum + 1):
            line.append((p1[0], y))

    if p1[1] == p2[1]:
        minimum = min([p1[0], p2[0]])
        maximum = max([p1[0], p2[0]])
        for x in range(minimum, maximum + 1):
            line.append((x, p1[1]))

    return line


def diagonalPoints(vector):
    p1, p2 = vector
    line = []

    lowest = p1
    other = p2
    if p2[0] < p1[0]:
        lowest = p2
        other = p1

    minimum = min([p1[0], p2[0]])
    maximum = max([p1[0], p2[0]])

    xdir = 1
    ydir = 1

    if other[0] - lowest[0] < 0:
        xdir = -1

    if other[1] - lowest[1] < 0:
        ydir = -1

    for i in range(0, maximum - minimum + 1):
        line.append((lowest[0] + (i * xdir), lowest[1] + (i * ydir)))

    return line


def isHorizVert(vector):
    p1, p2 = vector
    return p1[0] == p2[0] or p1[1] == p2[1]


def part1():
    overlap = set()

    for p in data:
        if not isHorizVert(p):
            continue
        line = set(vecPoints(p))

        # compare to other lines
        for p2 in data:
            if not isHorizVert(p2):
                continue
            line2 = set(vecPoints(p2))
            if line == line2:
                continue
            inter = line.intersection(line2)
            overlap = overlap.union(inter)
    return overlap


def part2():
    overlap = set()

    i = 0
    for p in data:
        line = None
        if isHorizVert(p):
            line = set(vecPoints(p))
        else:
            line = set(diagonalPoints(p))

        # compare to other lines
        j = 0
        for p2 in data:
            line2 = None
            if isHorizVert(p2):
                line2 = set(vecPoints(p2))
            else:
                line2 = set(diagonalPoints(p2))

            if i == j:
                continue
            inter = line.intersection(line2)
            overlap = overlap.union(inter)
            j += 1
        i += 1
    return overlap


"""
for p in data:
    if not isHorizVert(p):
        line = diagonalPoints(p)
        p1, p2 = p
        if p1 not in line:
            print("p1", p1, "not in line!", p1,
                  p2, line, "|", line[0], line[-1])
        if p2 not in line:
            print("p2", p2, "not in line!", p1, p2,
                  line, "|",  line[0], line[-1])
"""
start = time.time()

print(len(list(part1())))

t1 = time.time()
print("Part 1 done in ", (t1 - start))

print(len(list(part2())))

t2 = time.time()
print("Part 2 done in ", (t2 - t1))
print("Total done in", (t2 - start))
