input = open("input.txt").read().strip().splitlines()


def parse(line):
    return tuple(map(int, line.split("x")))


def area(tup):
    l, w, h = tup
    a = l * w
    b = w * h
    c = h * l
    return 2 * a + 2 * b + 2 * c + min([a, b, c])


def ribbon(tup):
    l, w, h = tup
    smallest = tuple(sorted(list(tup))[:2])
    a, b = smallest
    return (l * w * h) + (a * 2 + b * 2)


input = list(map(parse, input))

print(sum(map(area, input)))
print(sum(map(ribbon, input)))
