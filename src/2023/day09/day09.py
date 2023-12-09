def parse(line: str):
    return [int(x) for x in line.split(" ")]

input = list(map(parse, open("input.txt").readlines()))


# list of last 3 ints
def layer(ns: list[int]):
    return [ns[i + 1] - ns[i] for i in range(len(ns) - 1)]

def getLayers(ns: list[int]) -> list[list[int]]:
    layers = [ns]
    last = layers[-1]

    while sum(last) != 0:
        last = layer(last)
        layers.append(last)

    return layers

def answer(ns: list[int]):
    layers = getLayers(ns)
    last = [x[-1] for x in layers]
    return sum(last)

def part2(ns: list[int]):
    layers = getLayers(ns)
    first = [x[0] for x in layers]
    total = 0
    for row in reversed(first):
        #print(row, total, row - total)
        total = row - total
    #print()
    return total


ans = [answer(x) for x in input]
print(sum(ans))
print(sum([part2(x) for x in input]))