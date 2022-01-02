import math

input = int(open("input.txt").read().strip())

print(input)


def factors(n):
    return set(
        factor
        for i in range(1, int(n ** 0.5) + 1)
        if n % i == 0
        for factor in (i, n // i)
    )


def presentsAtHouse(houseNum):
    tot = 0
    for f in factors(houseNum):
        tot += f * 10

    return tot


def part2(houseNum):
    tot = 0
    for f in factors(houseNum):
        if houseNum // f <= 50:
            tot += f * 11
    return tot


print([(x, presentsAtHouse(x)) for x in range(1, 10)])

i = 1
while True:
    if presentsAtHouse(i) >= input:
        print(i)
        break
    i += 1

i = 1
while True:
    if part2(i) >= input:
        print(i)
        break
    i += 1