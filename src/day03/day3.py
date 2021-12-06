
data = list(map(list, open("input.txt").read().splitlines()))
#data = list(map(list, open("test.txt").read().splitlines()))
data3 = list(map(lambda x: x[::-1], zip(*data[::-1])))
data4 = list(map(lambda x: max(set(x), key=x.count), data3))
n2 = list(map(lambda x: str(~int(x) & 1), data4))
a = int(''.join(data4), 2)
b = int(''.join(n2), 2)
print(a * b)

# For the record: I FUCKING HATE THIS PART 2
# it is the most convoluted bullshit I have ever read
# and I am too lazy to make nice code to solve it
# I don't care about this part

rem = data
for i in range(0, len(data[0])):
    zeroes = 0
    ones = 0
    for n in rem:
        if n[i] == '0':
            zeroes += 1
        else:
            ones += 1
    if ones > zeroes or ones == zeroes:
        rem = list(filter(lambda x: x[i] == '1', rem))
    else:
        rem = list(filter(lambda x: x[i] == '0', rem))
    if len(rem) == 1:
        # print(rem)
        oxygen = int(''.join(rem[0]), 2)
        break

    # print("bit:", i + 1, "zeroes", zeroes, "ones", ones, "remainder", rem)

# print(oxygen)

rem = data
for i in range(0, len(data[0])):
    zeroes = 0
    ones = 0
    for n in rem:
        if n[i] == '0':
            zeroes += 1
        else:
            ones += 1
    if ones < zeroes:
        rem = list(filter(lambda x: x[i] == '1', rem))
    else:
        rem = list(filter(lambda x: x[i] == '0', rem))
    if len(rem) == 1:
        # print(rem)
        co2 = int(''.join(rem[0]), 2)
        break

    #print("bit:", i + 1, "zeroes", zeroes, "ones", ones, "remainder", rem)

print(oxygen * co2)
