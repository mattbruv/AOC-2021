

lines = list(map(str.strip, open("input.txt").readlines()))

words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def p1(string):
    ns = [char for char in string if char.isdigit()]
    return int(ns[0] + ns[-1])

def toNumbers(string):
    ns = []
    for i in range(0, len(string)):
        if string[i].isdigit():
            ns.append(string[i])
        else:
            test = string[i::]
            for idx, word in enumerate(words):
                if test.startswith(word):
                    ns.append(str(idx + 1))
                    i += len(word) 

    return int(ns[0] + ns[-1])

part1 = list(map(p1, lines))
part2 = list(map(toNumbers, lines))
print(sum(part1))
print(sum(part2))