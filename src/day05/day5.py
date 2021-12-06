def parsePoints(points):
    p1s = points[0].split(",")
    p2s = points[1].split(",")
    return [(int(p1s[0]), int(p1s[1])), (int(p2s[0]), int(p2s[1]))]


data = open("input.txt").read().splitlines()
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


def isHorizVert(vector):
    p1, p2 = vector
    return p1[0] == p2[0] or p1[1] == p2[1]


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

print(len(list(overlap)))
