import time

data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
data = list(map(int, open("input.txt").read().split(",")))


def distance(x, n):
    return abs(x - n)


def part2Distance(x, n):
    diff = abs(x - n)
    return sum(range(0, diff)) + diff


def getFuel(func, input, fromN):
    return map(lambda x: func(x, fromN), input)


ranges = list(range(min(data), max(data) + 1))


start = time.time()

fuels = map(lambda x: sum(getFuel(distance, data, x)), ranges)
print(min(fuels))
p1 = time.time()

fuelsP2 = map(lambda x: sum(getFuel(part2Distance, data, x)), ranges)
print(min(fuelsP2))
p2 = time.time()

print("Part 1 in", p1 - start)
print("Part 2 in", p2 - p1)
