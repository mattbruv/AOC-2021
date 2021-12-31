import collections

input = open("input.txt").read().strip().splitlines()


def isNice(string):
    vowels = "aeiou"
    counts = collections.Counter(string)
    bad = ["ab", "cd", "pq", "xy"]
    vowelCount = sum(map(lambda x: counts[x], vowels))

    if vowelCount < 3:
        return False

    for b in bad:
        if b in string:
            return False

    twiceTest = False
    prev = ""
    for chr in string:
        if chr == prev:
            twiceTest = True
        prev = chr

    return twiceTest


def isNice2(string):

    rule2 = False

    for i in range(0, len(string)):
        partial = string[i : i + 3]
        if len(partial) == 3:
            a, b, c = tuple(partial)
            if a == c:
                rule2 = True

    rule1 = False
    prev = ""
    counts = {}

    for i in range(0, len(string)):
        nextPair = string[i : i + 2]

        if nextPair == prev:
            continue
        prev = nextPair

        if nextPair not in counts:
            counts[nextPair] = 1
        else:
            counts[nextPair] += 1
        count = counts[nextPair]
        if count == 2:
            rule1 = True
            break

    return (rule1 != False) and (rule2 != False)


tests = [
    ("qjhvhtzxzqqjkmpb", True),
    ("xxyxx", True),
    ("uurcxstgmygtbstg", False),
    ("ieodomkazucvgmuy", False),
]

print(len(list(filter(isNice, input))))
print(len(list(filter(isNice2, input))))

for t in tests:
    s, res = t
    print("test:", s, "pass?", isNice2(s) == res)
