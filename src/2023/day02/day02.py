
lines = list(map(str.strip, open("input.txt").readlines()))

def parseRoll(roll:str):
    cubes = roll.split(",")
    cubes = [x.strip() for x in cubes]
    cubes = [(int(x.split(" ")[0]), x.split(" ")[1]) for x in cubes]
    return cubes

def parse(line:str):
    data = line.split(":")
    game = int(data[0].split(" ")[1])
    rolls = data[1].split(";")
    rolls = list(map(parseRoll, rolls))
    return (game, rolls)

def isValidPart1(roll):
    test = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    hands = roll[1]
    for hand in hands:
        for cube in hand:
            if cube[0] > test[cube[1]]:
                return False
    return True

data = list(map(parse, lines))

part1 = list(filter(isValidPart1, data))
part1 = [x[0] for x in part1]

print(sum(part1))