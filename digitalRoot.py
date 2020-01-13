def digitroot(n):
    if n < 10:
        return n
    return digitroot(n%10 + n//10)


print(digitroot(99999))
print(digitroot(10514))


