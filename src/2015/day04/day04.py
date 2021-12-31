import hashlib

input = open("input.txt").read().strip()


def findHash(zeroes):
    i = 0
    while True:
        s = input + str(i)
        out = hashlib.md5(s.encode()).hexdigest()
        if out[:zeroes] == "0" * zeroes:
            return i
        i += 1


print(findHash(5))
print(findHash(6))
