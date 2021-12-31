import collections

input = open("input.txt").read().strip()

counts = collections.Counter(input)
print(counts["("] - counts[")"])

i = 0
idx = 1
for x in input:
    if x == "(":
        i += 1
    else:
        i -= 1
    if i == -1:
        print(idx)
        break
    idx += 1
