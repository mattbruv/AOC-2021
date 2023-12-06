import sys
from functools import reduce
file = "input.txt"

if len(sys.argv) > 1 and sys.argv[1]:
    file = "test.txt"

input = open(file).readlines()

def parse(line: str):
    ns = line.split(":")[1].strip()
    return [int(n) for n in ns.split(" ") if n.isdigit()]

times = parse(input[0])
distance = parse(input[1])

def calculate(time: int, distance: int):
    xs = [i* (time - i) for i in range(1, time)]
    xs = [x for x in xs if x > distance]
    return len(xs)

part1 = list(map(lambda x: calculate(times[x], distance[x]), range(0, len(times))))
part1 = reduce(lambda x, y: x * y, part1)

print(part1)

time2 = int("".join([str(x) for x in times]))
distance2 = int("".join([str(x) for x in distance]))

part2 = calculate(time2, distance2)

print(part2)