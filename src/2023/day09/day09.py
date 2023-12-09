def parse(line: str):
    return [int(x) for x in line.split(" ")]

input = list(map(parse, open("input.txt").readlines()))


def answer(ns: list[int]):
    layers = [ns]
    last = layers[-1]

    while sum(last) != 0:
        last = layer(last)
        layers.append(last)

    last = [x[-1] for x in layers]
    return sum(last)


# list of last 3 ints
def layer(ns: list[int]):
    return [ns[i + 1] - ns[i] for i in range(len(ns) - 1)]

ans = [answer(x) for x in input]
print(sum(ans))