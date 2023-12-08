
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

def part1(obj):
    dirs = obj["dirs"]
    dir = 0
    current = "AAA"

    i = 0
    while current != "ZZZ":
        current = obj[current][dirs[dir]]
        i += 1
        dir = i % len(dirs)

    return i

print(part1(input))