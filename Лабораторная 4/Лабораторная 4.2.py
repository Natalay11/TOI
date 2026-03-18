import math

def muka(g: int):
    if g < 2:
        return False
    for i in range(2, int(math.sqrt(g)) + 1):
        if g % i == 0:
            return False
    return True

def prostye_chisla():
    n = 2
    while True:
        if muka(n):
            yield n
        n += 1

gen = prostye_chisla()
for _ in range(10):
    print(next(gen))
