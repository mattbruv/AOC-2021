data = open("data/day2.txt", 'r').read().splitlines()


def calculate(instrs):
    horiz = 0
    depth = 0
    for i in instrs:
        tup = i.split(" ")
        direction = tup[0]
        amount = int(tup[1])
        if direction == "down":
            depth += amount
        elif direction == "up":
            depth -= amount
        elif direction == "forward":
            horiz += amount
    return (horiz, depth)


def part2(instrs):
    aim = 0
    depth = 0
    horiz = 0
    for i in instrs:
        tup = i.split(" ")
        direction = tup[0]
        amount = int(tup[1])
        if direction == "down":
            aim += amount
        elif direction == "up":
            aim -= amount
        elif direction == "forward":
            horiz += amount
            depth += aim * amount
    return (horiz, depth)


res = calculate(data)
print(res[0] * res[1])
res = part2(data)
print(res[0] * res[1])
