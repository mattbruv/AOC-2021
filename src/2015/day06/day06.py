input = open("input.txt").read().strip().splitlines()

grid = {}


def parse(line):
    d = line.split()
    if d[0] != "toggle":
        d = d[1::]
    instr = d[0]
    frm = tuple(map(int, d[1].split(",")))
    to = tuple(map(int, d[3].split(",")))
    return (instr, frm, to)


input = list(map(parse, input))

for x in range(0, 1000):
    for y in range(0, 1000):
        grid[(x, y)] = False


for i in input:
    instr, frm, to = i
    x1 = frm[0]
    y1 = frm[1]
    x2 = to[0]
    y2 = to[1]

    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            if instr == "on":
                grid[(x, y)] = True
            elif instr == "off":
                grid[(x, y)] = False
            else:
                grid[(x, y)] = not grid[(x, y)]

ans1 = len([True for x in grid if grid[x] == True])


for x in range(0, 1000):
    for y in range(0, 1000):
        grid[(x, y)] = 0


for i in input:
    instr, frm, to = i
    x1 = frm[0]
    y1 = frm[1]
    x2 = to[0]
    y2 = to[1]

    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            idx = (x, y)
            val = grid[(x, y)]
            if instr == "on":
                grid[idx] += 1
            elif instr == "off":
                if val - 1 < 0:
                    grid[idx] = 0
                else:
                    grid[idx] = val - 1
            else:
                grid[idx] += 2

ans2 = sum([grid[x] for x in grid])

print(ans1)
print(ans2)
