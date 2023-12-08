import math

def parseNode(node: str):
    node = node.replace('(', '')
    node = node.replace(')', '')
    data = node.split(" = ")
    LR = data[1].split(",")
    obj = {
        "key": data[0],
        "L": LR[0].strip(),
        "R": LR[1].strip()
    }
    return obj


def parse(input: list[str]):

    nodeStrings = input[2::]

    nodes = [parseNode(x) for x in nodeStrings]

    obj = {
        "dirs": [x for x in input[0].strip()],
    }

    for node in nodes:
        obj[node["key"]] = {
            "L": node["L"],
            "R": node["R"],
        }

    return obj

input = parse(open("input.txt").readlines())

def part1(obj, start="AAA"):
    dirs = obj["dirs"]
    dir = 0
    current = start

    i = 0
    while current[-1] != "Z":
        current = obj[current][dirs[dir]]
        i += 1
        dir = i % len(dirs)

    return i

def part2(obj, starts):
    dirs = obj["dirs"]
    dir = 0
    keys = starts

    i = 0

    while not all([x[-1] == 'Z' for x in keys]):
        nextNode = []
        direction = dirs[dir]
        for node in keys:
            current = obj[node][direction]
            nextNode.append(current)

        keys = nextNode
        i += 1
        dir = i % len(dirs) 
        if i % 100000 == 0:
            print(i, keys)

    return i

# print(part1(input))

starts = [x for x in input.keys() if x[-1] == "A"]
ans = [part1(input, x) for x in starts]
print(ans)

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


factors = [prime_factors(x) for x in ans]
print(factors)

first = [x[0] for x in factors]
print(first)
i = 1
for n in first:
    i *= n

# 58,158,144,871 too small lol

print(ans)

lcm = math.lcm(*ans)
print(lcm)