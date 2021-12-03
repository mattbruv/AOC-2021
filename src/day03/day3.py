
data = list(map(list, open("input.txt").read().splitlines()))
data = map(lambda x: x[::-1], zip(*data[::-1]))
data = list(map(lambda x: max(set(x), key=x.count), data))
n2 = list(map(lambda x: str(~int(x) & 1), data))
a = int(''.join(data), 2)
b = int(''.join(n2), 2)
print(a * b)
