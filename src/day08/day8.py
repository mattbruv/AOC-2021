def parseLine(line):
    digits = line[0].split()
    numbers = line[1].split()
    return (digits, numbers)


data = list(map(lambda x: x.split(" | "), open(
    "input.txt").read().splitlines()))

data = list(map(parseLine, data))

print(data)
