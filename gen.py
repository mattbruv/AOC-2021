import requests
import os
import time

from requests.sessions import session

sessionCookie = ""
inputUrl = "https://adventofcode.com/{year}/day/{day}/input"

years = range(2015, 2022)
# years = range(2021, 2022)


def pad(day):
    return "{:02d}".format(day)


ins = []

for y in years:
    for day in range(1, 26):
        dayString = "day" + str(pad(day))
        path = "./src/" + str(y) + "/" + dayString + "/"
        reqUrl = inputUrl.format(year=y, day=day)
        i = path + "input.txt"
        ins.append(
            (
                str(y) + " " + str(day),
                len(open(i).read()),
                len(open(i).read().splitlines()),
            )
        )

out = sorted(ins, key=lambda x: x[1])
open("input-len.txt", "w").write("\n".join(list(map(str, out))))
