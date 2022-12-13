from itertools import combinations

i = list(map(int, open("input.txt").read().splitlines()))

p1 = (next(filter(lambda x: sum(x) == 2020, combinations(i, 2))))
print(p1[0] * p1[1])

p1 = (next(filter(lambda x: sum(x) == 2020, combinations(i, 3))))
print(p1[0] * p1[1] * p1[2])
