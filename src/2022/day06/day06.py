
def solve(signal, n):
    return next(i for i in range(len(signal)) if len(set(signal[i:i+n])) == n) + n


def test():
    tests = [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7, 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5, 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6, 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10, 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11, 26),
    ]

    for t in tests:
        res = solve(t[0], 4)
        p1 = t[0][0:res]
        p2 = t[0][res:len(t[0])]
        print(res == t[1], res, "==", t[1], p1, p2)
        p2 = solve(t[0], 14)
        print(p2 == t[2], p2, t[2])


input = open("input.txt").read()

# test()

print(solve(input, 4))
print(solve(input, 14))
