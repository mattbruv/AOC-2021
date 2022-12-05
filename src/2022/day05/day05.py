from textwrap import wrap
from collections import deque
from typing import List


def parseCrate(line):
    crates = wrap(line, 4, drop_whitespace=False)
    crates = list(zip(crates, range(0, len(crates))))
    crates = [x for x in crates if x[0] != "    "]
    indicies = [x[1] for x in crates]
    crates = [x[0][1] for x in crates]
    return (crates, indicies)


def parseMove(line):
    d = line.split()
    return (int(d[1]), int(d[3]) - 1, int(d[5]) - 1)


input = open("input.txt").read()
crates, moves = input.split("\n\n")

crates = list(map(parseCrate, crates.splitlines()[:-1]))
moves = list(map(parseMove, moves.splitlines()))


def addCrate(crates: List[deque], layout):
    chars, idxs = layout
    for i in range(0, len(chars)):
        crates[idxs[i]].append(chars[i])


def part1(layout, moves):
    crates = [deque() for x in range(0, 9)]
    layout.reverse()

    for item in layout:
        addCrate(crates, item)

    for move in moves:
        cuanto, de, a = move
        out = []
        for _ in range(cuanto):
            out.append(crates[de].pop())
        out.reverse()
        for item in out:
            crates[a].append(item)

    return "".join([x[-1] for x in crates])


print(part1(crates, moves))
