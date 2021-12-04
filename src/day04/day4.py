import math


def parseBoard(board):
    return list(map(parseBoardRow, board))


def parseBoardRow(row):
    return list(map(int, row.strip().split()))


def bools(board):
    return [(x, False) for x in [y for y in board]]


data = list(map(lambda x: x.splitlines(), open(
    "input.txt").read().split("\n\n")))

drawnNumbers = list(map(int, data[0][0].split(",")))
boards = list(map(parseBoard, data[1:]))
boards = list(map(bools, boards))

print(boards)
