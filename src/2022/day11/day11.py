
data = (
    (
        (91, 58, 52, 69, 95, 54),
        lambda x: x * 13,
        lambda x: x % 7 == 0,
        1,
        5
    ),
    (
        (80, 80, 97, 84),
        lambda x: x * x,
        lambda x: x % 3 == 0,
        3,
        5
    ),
    (
        (86, 92, 71),
        lambda x: x + 7,
        lambda x: x % 2 == 0,
        0,
        4
    ),
    (
        (96, 90, 99, 76, 79, 85, 98, 61),
        lambda x: x + 4,
        lambda x: x % 11 == 0,
        7,
        6
    ),
    (
        (60, 83, 68, 64, 73),
        lambda x: x * 19,
        lambda x: x % 17 == 0,
        1,
        0
    ),
    (
        (96, 52, 52, 94, 76, 51, 57),
        lambda x: x + 3,
        lambda x: x % 5 == 0,
        7,
        3
    ),
    (
        (75,),
        lambda x: x + 5,
        lambda x: x % 13 == 0,
        4,
        2
    ),
    (
        (83, 75),
        lambda x: x + 1,
        lambda x: x % 19 == 0,
        2,
        6
    ),
)

monkeyList = [[[x for x in y[0]], 0] for y in data]


def round(monkeys):
    for i in range(len(monkeys)):
        m = monkeys[i]
        for j in range(len(m[0])):
            item = m[0].pop()
            after = data[i][1](item) // 3
            cond = data[i][2](after)
            t = data[i][3]
            f = data[i][4]
            idx = t if cond else f
            monkeys[idx][0].append(after)
            monkeys[i][1] += 1


for i in range(0, 20):
    round(monkeyList)

print(monkeyList)
top = sorted([x[1] for x in monkeyList])[::-1][0:2]
print(top[0] * top[1])
