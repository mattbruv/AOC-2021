input = open("input.txt").read().splitlines()


def parseNums(n):
    ns = n.split("-")
    l = int(ns[0])
    r = int(ns[1])
    return (l, r)


def parseLine(line):
    sides = line.split(",")
    sides = list(map(parseNums, sides))
    return sides


def contains(n1, n2):
    return n1[0] >= n2[0] and n1[1] <= n2[1]


def contains2(n):
    n1, n2 = n
    return n2[0] <= n1[1] and n2[1] >= n1[0]


input = list(map(parseLine, input))

part1 = list(filter(lambda x: contains(
    x[0], x[1]) or contains(x[1], x[0]), input))

part2 = list(filter(lambda x: contains2(x), input))

print(len(part1))
print(len(part2))
