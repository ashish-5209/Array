def rec(n):
    if n == 0:
        return
    else:
        print(n, end=" ")
        return rec(n-1)


rec(5)