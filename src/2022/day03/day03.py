input = open("input.txt").read().strip().splitlines()
test = open("test.txt").read().strip().splitlines()


def charVal(char: str):
    lower = ord(char) - ord('a') + 1
    upper = ord(char) - ord('A') + 27
    return lower if char.islower() else upper


def parseLine(line):
    half = len(line) // 2
    h1 = line[0:half]
    h2 = line[half:len(line)]
    return (h1, h2)


def getShared(lists):
    chars = list(set(lists[0]).intersection(set(lists[1])))
    return list(map(charVal, chars))


def part1():
    data = map(parseLine, input)
    data = list(map(getShared, data))
    flat_list = [item for sublist in data for item in sublist]
    return sum(flat_list)


def parsePart2(group):
    a = set(group[0])
    b = set(group[1])
    c = set(group[2])
    value = a.intersection(b).intersection(c)
    return charVal(list(value)[0])


def part2():
    data = list(zip(*(iter(input),) * 3))
    data = list(map(parsePart2, data))
    return sum(data)


print(part1())
print(part2())
