
"""
THIS CODE IS REALLY SLOPPY AND BAD
I just wanted to solve this problem as fast as possible
I ranked 4,869 for both problems solved, in like 38 minutes
I just wanted to code it as fast as possible to see how quick
I could come up with a solution
"""

data = open("input.txt").read().splitlines()
test = data[0]


syntax = ["()", "[]", "{}", "<>"]
syntax = list(map(lambda x: (x[0], x[1]), syntax))
openers = [x[0] for x in syntax]
closers = [x[1] for x in syntax]


def firstError(line):
    lastOpener = []
    for c in line:
        if c in openers:
            lastOpener.append(c)
        else:
            expected = closers[openers.index(lastOpener[-1])]
            if c != expected:
                return c
            else:
                lastOpener.pop()
    return None


def fix(line):
    lastOpener = []
    for c in line:
        if c in openers:
            lastOpener.append(c)
        else:
            lastOpener.pop()
    lastOpener.reverse()
    lastOpener = list(map(lambda x: closers[openers.index(x)], lastOpener))
    return ''.join(lastOpener)


vals = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

counts = {}
for d in data:
    err = firstError(d)
    if err:
        if err not in counts:
            counts[err] = 1
        else:
            counts[err] += 1

i = 0
for c in counts:
    i += vals[c] * counts[c]

print(i)

incompletes = list(filter(lambda x: firstError(x) == None, data))

points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

scores = []

for i in incompletes:
    score = 0
    chars = fix(i)
    for c in chars:
        score *= 5
        val = points[c]
        score += val
    #print(chars, score)
    scores.append(score)

scores.sort()

print(scores[len(scores) // 2])
