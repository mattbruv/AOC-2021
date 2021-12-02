import random

# Top 50 languages from https://www.tiobe.com/tiobe-index/ for november 2021
langs = open('langs/langs.txt').read().splitlines()

for i in range(0, 2021):
    random.shuffle(langs)

for i in range(0, 25):
    print(str(i + 1) + ": " + langs[i])
