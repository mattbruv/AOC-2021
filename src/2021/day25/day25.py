data = open("test.txt").read().splitlines()
print(data)

width = len(data[0])
height = len(data)
print(width, height)
