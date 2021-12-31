from itertools import combinations

input = list(map(int, open("input.txt").read().strip().splitlines()))

count = 0

comboSet = set()
for i in range(2, len(input)):
    combos = combinations(input, r=i)
    for c in combos:
        if sum(c) == 150:
            comboSet.add(c)
            count += 1

print(count)

minContainers = len(sorted(comboSet, key=len)[0])

print(
    len(
        list(filter(lambda x: x == 150, map(sum, combinations(input, r=minContainers))))
    )
)
