from collections import Counter


current = ['A', 'b', 'c', 'b']
nodes = set(['b', 'c', 'd'])


def getNextOptions(current, nodes):
    counts = Counter(filter(lambda x: x.lower() == x, current))
    visits = [counts[x] for x in counts]
    if 2 not in visits:
        options = [x for x in counts if counts[x] == 1]
    else:
        options = nodes.difference()  # lowers
    print(visits)
    print(counts)
    print(options)


print(getNextOptions(current, nodes))
