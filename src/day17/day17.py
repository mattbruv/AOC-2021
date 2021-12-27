
xMin = 288
xMax = 330
yMin = -96
yMax = -50

def inX(x):
    return x >= xMin and x <= xMax

def inY(y):
    return y >= yMin and y <= yMax

def inBounds(x, y):
    return inX(x) and inY(y)

def pastX(x):
    return x > xMax

def pastY(y):
    return y < yMin


def pastBounds(x, y):
    return pastX(x) or pastY(y)

def step(x, y, xVel, yVel, peak, steps):

    if inBounds(x, y):
        return peak

    if pastBounds(x, y):
        return -1
    tempX = x + xVel
    
    if xVel > 0:
        xVel -= 1
    elif xVel < 0:
        xVel += 1
    else:
        xVel = 0
    
    if y > peak:
        peak = y
    
    return step(tempX, y + yVel, xVel, yVel - 1, peak, steps + 1)

def shoot(xVel, yVel):
    return step(0, 0, xVel, yVel, 0, 0)

def xVelDist(x):
    if x <= 1:
        return x
    return x + xVelDist(x - 1)

testRange = list(range(-100, 101))
searchY = list(range(-500, 501))
searchXs = list(range(-100, 101))

def peaks(x) -> bool:
    return x > 0

searchX = list(filter(lambda x: inX(xVelDist(x)), testRange))
print(searchX)

def maxAtX(x):
    #print(searchY)
    a = list(map(lambda y: shoot(x, y), searchY))
    #print(a)
    b = list(filter(peaks, a))
    if len(b) == 0:
        return 0
    return max(b)

def peakAtX (x):
    return list(filter(peaks, map(lambda y: shoot(x, y), searchY)))

def part2(x):
    return len(peakAtX(x))

print(max(list(map(maxAtX, searchX))))
print(sum(list(map(part2, searchXs))))