input = open("input.txt").read().strip()

x = 0
y = 0

counts = {}

counts[(x, y)] = 1

for move in input:
    if move == ">":
        x += 1
    elif move == "<":
        x -= 1
    elif move == "^":
        y += 1
    elif move == "v":
        y -= 1
    if (x, y) in counts:
        counts[(x, y)] += 1
    else:
        counts[(x, y)] = 1

print(len(counts))


x = 0
y = 0
a = 0
b = 0

counts = {}

counts[(x, y)] = 1
counts[(a, b)] += 1

n = 0
for move in input:
    dx = 0
    dy = 0
    if move == ">":
        dx += 1
    elif move == "<":
        dx -= 1
    elif move == "^":
        dy += 1
    elif move == "v":
        dy -= 1

    tx = 0
    ty = 0

    if n % 2 == 0:
        x += dx
        y += dy
        tx = x
        ty = y
    else:
        a += dx
        b += dy
        tx = a
        ty = b

    if (tx, ty) in counts:
        counts[(tx, ty)] += 1
    else:
        counts[(tx, ty)] = 1

    n += 1

print(len(counts))
