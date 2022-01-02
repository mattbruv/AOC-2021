input = open("input.txt").read().strip().splitlines()


def parse(line):
    d = line.split("for")
    d = list(map(lambda x: x.strip(), d))
    a = int(d[1].split()[0])
    b = int(d[2].split()[0])
    n1 = int(d[0].split()[3])
    return (n1, a, b)


input = list(map(parse, input))


def distance(deer, seconds):
    speed, goTime, restTime = deer
    lapTime = restTime + goTime
    total = (seconds // lapTime) + 1
    rem = seconds % lapTime + 1
    adjust = 0
    if rem <= goTime:
        adjust = (goTime - rem) * speed
    return total * speed * goTime - adjust


print(max(list(map(lambda x: distance(x, 2503), input))))

scores = {}

for i in input:
    scores[i] = 0

for seconds in range(0, 2504):
    deerScores = list(map(lambda x: (x, distance(x, seconds)), input))
    best = max([x[1] for x in deerScores])
    deers = [x[0] for x in deerScores if x[1] == best]
    for d in deers:
        scores[d] += 1

print(max([scores[x] for x in scores]))
