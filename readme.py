

for i in range(1, 26):
    s = str(i)
    a = "- [ ] - [ ] [Day " + s + \
        "](https://adventofcode.com/2021/day/" + s + ")"
    b = "[src](./src/day" + s + ")"
    c = a + " - " + b
    print(c)
