"""
BEWARE ALL YE WHO ENTER THIS WRETCHED FILE

My solution to part 1 was so ugly that I didn't even
bother with making either part into some kind of function
So if you want to see part 1 or part 2, toggle the variable
in the traverse() function.

But let's be honest, you really should just turn back now.
"""


from collections import Counter
import time

data = open("input.txt").read().splitlines()

start = time.time()


def parseData(data):
    caveMap = {}
    for d in data:
        start, end = d.split("-")
        if start not in caveMap:
            caveMap[start] = [end]
        else:
            caveMap[start].append(end)
        if end not in caveMap:
            caveMap[end] = [start]
        else:
            caveMap[end].append(start)
    caveMap["end"] = []
    #del caveMap["start"]
    for i in caveMap:
        if "start" in caveMap[i]:
            caveMap[i].remove("start")

    return caveMap


def smallCaves(nodes):
    return set(filter(lambda x: x == x.lower(), nodes))


def traverse(node, caveMap, trails, current, part1=True):
    if part1:
        nextNodes = set(caveMap[node])
        nextNodes = nextNodes.difference(smallCaves(current))
    else:
        nextNodes = set(caveMap[node])
        counts = Counter(filter(lambda x: x.lower() == x, current))
        visits = [counts[x] for x in counts]
        # print(nextNodes)
        if 2 not in visits:
            # print("no small cave visited twice:")
            a = set([x for x in counts if counts[x] == 1])
            b = smallCaves(current)
            c = b.difference(a)
            nextNodes = nextNodes.difference(c)
        else:
            # print("small cave visited twice")
            nextNodes = nextNodes.difference(smallCaves(current))  # lowers
    # print(node, caveMap[node])
    # print(nextNodes)

    # are we at the end?
    if len(nextNodes) == 0:
        # add current path
        trails.append(current.copy())
        return

    for nextNode in nextNodes:
        current.append(nextNode)
        traverse(nextNode, caveMap, trails, current, part1)
        # print(nextNode)
        current.pop()

    return trails


def isFullRoute(route):
    return "end" in route


caveMap = parseData(data)

routes = []
for startNode in caveMap["start"]:
    routeList = list(filter(isFullRoute, traverse(
        startNode, caveMap, [], [startNode], part1=False)))
    for r in routeList:
        r = ["start"] + r
        if r not in routes:
            routes.append(r)


for r in routes:
    print(','.join(r))

print(len(routes))

end = time.time()
print("Done in", end - start)
