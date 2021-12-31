import itertools
import collections


def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def parseMap(polyMap):
    pMap = {}
    for x in polyMap:
        f, t = x.split(" -> ")
        pMap[f] = t
    return pMap


data = open("input.txt").read().split("\n\n")

template = data[0]
polyMap = parseMap(data[1].splitlines())


def getInsertions(template):
    pairs = list(pairwise(template))
    replace = list(map(lambda x: polyMap[''.join(x)], pairs))
    for i in range(0, len(pairs)):
        x = pairs[i][1]
        pairs[i] = pairs[i][0] + replace[i]  # + pairs[i][1]
        if i == len(pairs) - 1:
            pairs[i] += x
    return ''.join(pairs)


def part1():
    x = template
    for i in range(0, 10):
        x = getInsertions(x)
        print(i + 1, len(x))
    counts = collections.Counter(x)
    maximum = counts[max(counts, key=lambda x: counts[x])]
    minimum = counts[min(counts, key=lambda x: counts[x])]
    return maximum - minimum


polyCount = {}
for x in polyMap:
    polyCount[x] = 0

# seed the initial data
seed = list(pairwise(template))
seed = list(map(lambda x: ''.join(x), seed))
for s in seed:
    polyCount[s] += 1


def iterate(polyMap, polyCount: dict, charCount: dict):
    keys = list(filter(lambda x: polyCount[x] > 0, polyCount))
    newCount = polyCount.copy()
    for k in keys:
        replace = polyMap[k]
        # print(k, "->", replace)
        left = k[0] + replace
        right = replace + k[1]
        times = polyCount[k]
        newCount[left] += times
        newCount[right] += times
        newCount[k] -= times
        # print(left, right)
        #print(left, right, "|", k[0], replace, k[1])
        # charCount[k[0]] += times
        # charCount[k[1]] += times
        charCount[replace] += times
        # add to counts
        # print()
    return newCount


print(template)
print()
print(polyCount)
print()
print(polyMap)

charCount = {}
keys = set([x for x in ''.join(polyMap.keys())])
for x in keys:
    charCount[x] = 0

for c in template:
    charCount[c] += 1

newCount = polyCount.copy()

# CHANGE LOOP ITERATIONS TO GET ANSWERS FOR PART 1/2
for i in range(0, 40):
    newCount = iterate(polyMap, newCount, charCount)

for c in newCount:
    if newCount[c] > 0:
        print(c, ":", newCount[c])

print(charCount)
counts = list(map(lambda x: charCount[x], charCount))

print("Total characters:", "{:,}".format(sum(counts)))

print(max(counts) - min(counts))
