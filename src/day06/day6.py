data = list(map(int, open("input.txt").read().split(",")))

fish = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0
}

for x in data:
    fish[x] += 1


def simulateFish(fish, days):
    for i in range(0, days):
        newFish = fish[0]
        for x in range(1, len(fish)):
            fish[x - 1] = fish[x]
        fish[6] += newFish
        fish[8] = newFish


simulateFish(fish, 80)
print(sum(fish[x] for x in fish))

simulateFish(fish, 256 - 80)
print(sum(fish[x] for x in fish))
