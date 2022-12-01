

input = open("input.txt").read()

input = input.replace("\n\n", "\n-1\n")

input = input.splitlines()

input = list(map(lambda x: ".long " + x, input))

open("input.s", "w+").write('\n'.join(input))

print(input)
