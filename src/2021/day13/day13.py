data = open("input.txt").read().split("\n\n")

dots = data[0].splitlines()
dots = list(map(lambda x: x.split(","), dots))
dots = list(map(lambda x: (int(x[0]), int(x[1])), dots))
folds = data[1].splitlines()
folds = list(
    map(lambda x: (x.split("=")[0][-1], int(x.split("=")[1])), folds))

width = max(map(lambda x: x[0], dots)) + 1
height = max(map(lambda x: x[1], dots)) + 1

print(width, "x", height)


def dotsToPaper(dots):
    paper = []
    for i in range(0, height):
        row = []
        for j in range(0, width):
            row.append(0)
        paper.append(row)
    for dot in dots:
        x, y = dot
        paper[y][x] += 1
    return paper


def getPointChar(point):
    if point > 0:
        return "#"
    return "."


def printPaper(paper):
    for line in paper:
        s = ''.join(map(getPointChar, line))
        print(s)
    print()


def rotate90(original):
    res = list(zip(*original[::-1]))
    return list(map(list, res))


def overlapLists(smallList, bigList):
    print(len(smallList), len(bigList))
    if len(smallList[0]) != len(bigList[0]):
        exit("ERROR, LISTS ARE NOT SAME SIZE")
    smallRev = list(smallList)
    bigRev = list(reversed(bigList))
    for line in range(0, len(smallRev)):
        for dot in range(0, len(smallRev[line])):
            if smallRev[line][dot] > 0:
                bigRev[line][dot] += smallRev[line][dot]

    return list(reversed(bigRev))


small = [
    [1, 1, 1, 1],
    [10, 10, 10, 10],
    [3, 3, 3, 3],
]

big = [
    [10, 10, 10, 10],
    [11, 11, 11, 11],
    [12, 12, 12, 12],
    [13, 13, 13, 13],
    [14, 14, 14, 14],
]

#res = overlapLists(small, big)
# print(res)


def foldUp(paper, atLine):
    top = paper[0:atLine]
    bottom = paper[atLine+1::]
    smallList = None
    bigList = None
    print("paper rows", len(paper), "at line:", atLine, len(top), len(bottom))
    if (len(top) > len(bottom)):
        bigList = top
        smallList = bottom
    else:
        smallList = top
        bigList = bottom
    res = overlapLists(smallList, bigList)

    return list(reversed(res))


def foldLeft(paper, atLine):
    rot = rotate90(paper)
    rot = foldUp(rot, atLine)
    rot = rotate90(rot)
    rot = rotate90(rot)
    rot = rotate90(rot)
    return rot


def countDotsOnLine(line):
    return sum([1 for x in line if x > 0])


def countDots(paper):
    return sum(map(countDotsOnLine, paper))


fs = {'x': foldLeft, 'y': foldUp}

paper = dotsToPaper(dots)
for fold in folds:
    way, atLine = fold
    paper = fs[way](paper, atLine)

printPaper(paper)
print(countDots(paper))

print(folds)
