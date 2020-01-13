import math
def digitCount(n):
    if n == 0:
        return 0
    else:
        return 1 + digitCount(n // 10)


def dCount(n):
    return math.floor(math.log(n, 10) + 1)


print(digitCount(8774646756))
print(dCount(8774646756))