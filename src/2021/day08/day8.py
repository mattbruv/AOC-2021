from collections import Counter

uniqueChars = [(2, 1), (3, 7), (4, 4), (7, 8)]


def parseLine(line):
    digits = line[0].split()
    numbers = line[1].split()
    return (digits, numbers)


def decodeLine(line):
    digits, nums = line
    counts = Counter("".join(digits))
    chars = {}
    segments = {}
    segments[2] = set([item for item in counts if counts[item] == 6][0])
    segments[5] = set([item for item in counts if counts[item] == 4][0])
    segments[6] = set([item for item in counts if counts[item] == 9][0])

    for d in digits:
        x = list(filter(lambda x: x[0] == len(d), uniqueChars))
        if x:
            chars[x[0][1]] = set(d)

    segments[4] = chars[4].difference(chars[1], segments[2])
    segments[1] = chars[7].difference(chars[1])
    chars[0] = chars[8].difference(segments[4])
    chars[3] = chars[8].difference(segments[2], segments[5])
    chars[9] = chars[8].difference(segments[5])
    chars[2] = chars[8].difference(segments[2], segments[6])
    segments[3] = chars[7].difference(segments[1], segments[6])
    chars[6] = chars[8].difference(segments[3])
    chars[5] = chars[6].difference(segments[5])

    return chars


def part1(line):
    digits, nums = line
    uniqueLens = [idx[0] for idx in uniqueChars]
    res = list(map(len, filter(lambda x: len(x) in uniqueLens, nums)))
    return len(res)


def part2(line):
    chars = decodeLine(line)
    digits, nums = line
    s = ""
    for n in nums:
        decoded = [idx for idx in chars if chars[idx] == set(n)][0]
        s += str(decoded)
    return int(s)


data = open("input.txt").read().splitlines()
data = list(map(lambda x: x.split(" | "), data))
data = list(map(parseLine, data))

print(sum(map(part1, data)))
print(sum(map(part2, data)))
