import requests
import os
import time

from requests.sessions import session

sessionCookie = ""
inputUrl = "https://adventofcode.com/{year}/day/{day}/input"

years = range(2015, 2021)
# years = range(2021, 2022)


def pad(day):
    return "{:02d}".format(day)


for y in years:
    for day in range(1, 26):
        dayString = "day" + str(pad(day))
        path = "./src/" + str(y) + "/" + dayString + "/"
        reqUrl = inputUrl.format(year=y, day=day)
        # data = requests.get(reqUrl, cookies={"session": sessionCookie})
        # problemInput = data.text.strip()
        print(path)
        # data = open(path + "input.txt").read().strip()
        data = """input = open("input.txt").read().strip()

print("{year} day {day}")""".format(
            year=y, day=day
        )
        open(path + "day" + pad(day) + ".py", "w").write(data)
        # time.sleep(0.5)
