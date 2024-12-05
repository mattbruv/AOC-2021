from collections import Counter

def parse_the_fucking_rules(rule):
    a = rule.split("|")
    return (int(a[0]), int(a[1]))

def parse_the_fucking_updates(update: str):
    splits = update.split(",")
    return list(map(int, splits))

input = open("input.txt").read()

split = input.split("\n\n")

top = split[0].splitlines()
bottom = split[1].splitlines()

rules = list(map(parse_the_fucking_rules, top))
updates = list(map(parse_the_fucking_updates, bottom))

befores = list(map(lambda x: x[0], rules))
afters = list(map(lambda x: x[1], rules))

# for each number, have a list of before and afters
maps = {

}

def add(n):
    if n not in maps:
        maps[n] = {
            "before": set(),
            "after": set()
        }

for (before, after) in rules:
    add(before)
    add(after)

    maps[before]["before"].add(after)
    maps[after]["after"].add(before)

def is_indirectly_before(a, b, visited=None) -> bool:
    if visited is None:
        visited = set()
    if a == b:  # If we somehow compare the same element
        return True
    if is_directly_before(a, b):  # Direct relationship
        return True
    if a in visited:  # Prevent revisiting nodes in cycles
        return False
    visited.add(a)
    return any(is_indirectly_before(x, b, visited) for x in maps[a]["before"])


"""
def is_indirectly_before(a, b) -> bool:
    if is_directly_before(a, b):
        return True
    else:
        afters = maps[a]["before"]
        print(a, b, afters)
        if len(afters) > 0:
            return any(map(lambda x: is_indirectly_before(x, b), afters))
        return False
        """

def is_directly_before(a, b) -> bool:
    return b in maps[a]["before"]

# TEMPORARY
#maps[47]["before"].remove(29)
#maps[61]["before"].remove(29)
#print(is_indirectly_before(47, 29))

def in_order(update):
    if len(update) > 1:
        first = update[0]
        second = update[1]
        rest = update[1:]
        print(first, second, rest)
        if is_indirectly_before(first, second):
            return in_order(rest)
        else:
            return False
    return True

for update in updates:
    print(in_order(update))

# first attempt, failed because actual input are all 24 on left and 24 on right
"""
counts = Counter(afters)
before_counts = Counter(befores)

order = sorted(list(counts.items()), key=lambda x: x[1])
append = list(set([x for x in befores if x not in afters]))
order = append + list(map(lambda x: x[0], order))

def in_order(question: list[int], target: list[int]):
    filtered = list([x for x in target if x in question])
    return question == filtered

def middle(l: list[int]) -> int:
    x = len(l)
    idx = x // 2
    return l[idx]

ans = list(filter(lambda x: in_order(x, order), updates))

print(counts)
print(before_counts)
"""