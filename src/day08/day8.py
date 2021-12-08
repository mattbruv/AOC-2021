def parseLine(line):
    digits = line[0].split()
    numbers = line[1].split()
    return (digits, numbers)


data = list(map(lambda x: x.split(" | "), open(
    "input.txt").read().splitlines()))

data = list(map(parseLine, data))


def decodeLine(line):
    print(line)


a = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab"
b = "cdfeb fcadb cdfeb cdbaf"

data = (a.split(), b.split())
print(data)

# for d in data:
#    print(decodeLine(d))
