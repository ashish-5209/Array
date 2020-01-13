def cuts(n, a, b, c):
    if n == 0:
        return 0
    if n < 0:
        return -1

    res = max(cuts(n-a, a, b, c),
              cuts(n-b, a, b, c),
              cuts(n-c, a, b, c))

    return -1 if res == -1 else res + 1


print(cuts(23, 11, 9, 12), [...])
