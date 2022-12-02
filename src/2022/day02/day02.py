import time

input = open("input.txt").read().strip()

L = 0
D = 3
W = 6

result = [
    (1, [D, L, W]),  # rock
    (2, [W, D, L]),  # paper
    (3, [L, W, D]),  # scissors
]


def part1(hand):
    them = ord(hand[0]) - 65
    me = ord(hand[1]) - 23 - 65
    res = result[me][0] + result[me][1][them]
    return res


def part2(hand):
    them = ord(hand[0]) - 65
    res = (ord(hand[1]) - 88) * 3
    add = res
    if res == 6:
        res = 0
    else:
        if res == 0:
            res = 6
    choice = result[them][1].index(res)
    #print(hand, them, "result:", res, "pick:", choice, add + choice + 1)
    return add + choice + 1


start_time = time.time()
part1 = list(map(lambda x: part1(x.split()), input.splitlines()))
part2 = list(map(lambda x: part2(x.split()), input.splitlines()))
end_time = time.time()

print(sum(part1))
print(sum(part2))

print(end_time - start_time, "seconds")
