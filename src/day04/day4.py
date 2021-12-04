def parseBoard(board):
    board = " ".join(board)
    board = list(map(lambda x: (int(x), False), board.split()))
    return board


def markNumber(board, number):
    for i in range(0, len(board)):
        num, val = board[i]
        if number == num:
            board[i] = (num, True)


data = list(map(lambda x: x.splitlines(), open(
    "input.txt").read().split("\n\n")))

drawnNumbers = list(map(int, data[0][0].split(",")))
boards = list(map(parseBoard, data[1:]))


def isWinning(board):
    return scanHoriz(board) or scanVert(board)


def scanVert(board):
    for x in range(0, 5):
        for y in range(0, 5):
            num, val = board[y * 5 + x]
            if val == False:
                break
            if y == 4:
                return True
    return False


def scanHoriz(board):
    for i in range(0, 5):
        if len(list(filter(lambda x: x[1] == True, board[i * 5:(i * 5 + 5)]))) == 5:
            return True
    return False


def unmarkedSum(board):
    return sum(list(map(lambda x: x[0], filter(lambda x: x[1] == False, board))))


def printBoard(board):
    for y in range(0, 5):
        print(board[y*5:y*5+5])


winners = []
sums = []

for n in drawnNumbers:
    for b in boards:
        markNumber(b, n)
        if isWinning(b):
            if b not in winners:
                winners.append(b)
                sums.append(unmarkedSum(b) * n)

print(sums[0])
print(sums[-1])
