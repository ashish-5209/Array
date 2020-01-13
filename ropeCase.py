def rope(n):
    if n <= 0:
        return 0
    else:
        return 1 + rope(n-1) + rope(n-2) + rope(n-5)


print(rope(5))