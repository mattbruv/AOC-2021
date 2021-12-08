from collections import Counter


def parseLine(line):
    digits = line[0].split()
    numbers = line[1].split()
    return (digits, numbers)


data = open("input.txt").read().splitlines()
data = list(map(lambda x: x.split(" | "), data))
data = list(map(parseLine, data))

# (segments, number)
uniqueChars = [(2, 1), (3, 7), (4, 4), (7, 8)]

# segment -> number of times it appears in 0-10
segs = {
    # 1: 8,
    2: 6,
    # 3: 8,
    # 4: 7,
    5: 4,
    6: 9,
    # 7: 7
}


def decodeLine(line):
    digits, nums = line

    chars = {}
    segments = {}

    all = "".join(digits)
    counts = Counter(all)
    # newList = [expression for item in iterable if condition == True]
    segments[2] = set([item for item in counts if counts[item] == 6][0])
    segments[5] = set([item for item in counts if counts[item] == 4][0])
    segments[6] = set([item for item in counts if counts[item] == 9][0])

    for i in range(0, 10):
        chars[i] = set()

    # get characters for unique numbers
    for d in digits:
        l = len(d)
        x = list(filter(lambda x: x[0] == l, uniqueChars))
        if x:
            chars[x[0][1]] = set(d)

    # middle segment
    segments[4] = chars[4].difference(chars[1], segments[2])
    segments[1] = chars[7].difference(chars[1])

    # now we know 0
    chars[0] = chars[8].difference(segments[4])
    # and 3
    chars[3] = chars[8].difference(segments[2], segments[5])
    chars[9] = chars[8].difference(segments[5])
    chars[2] = chars[8].difference(segments[2], segments[6])

    segments[3] = chars[7].difference(segments[1], segments[6])

    chars[6] = chars[8].difference(segments[3])
    chars[5] = chars[6].difference(segments[5])

    """
    for c in chars:
        print(c, chars[c])

    print()
    for s in sorted(segments):
        print(s, segments[s])
    """

    s = ""
    for n in nums:
        # newList = [expression for item in iterable if condition == True]
        decoded = [idx for idx in chars if chars[idx] == set(n)][0]
        s += str(decoded)
    return int(s)


# a = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab"
# b = "cdfeb fcadb cdfeb cdbaf"
# data = (a.split(), b.split())

print(sum(map(decodeLine, data)))

# for d in data:
#    print(decodeLine(d))
