from collections import Counter

def parse(line: str):
    data =  line.split()
    return ([x for x in data[0]], int(data[1]))

input = list(map(parse, open("input.txt").readlines()))

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


def rank(card: str):
    return ranks.index(card)

def fiveOfKind(hand: Counter):
    return len(hand.keys()) == 1

def fourOfKind(hand: Counter):
    return len(hand.keys()) == 2

def threeOfKind(hand: Counter):
    return len(hand.keys()) == 3



first = Counter(input[0][0])
print(fiveOfKind(first))
print(fourOfKind(first))
print(threeOfKind(first))


