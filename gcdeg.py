def gcd(n, m):

    if n % m == 0:
        return m
    else:
        return gcd(m, n%m)


n = int(input())
count = 0
for i in range(1, n):

    if gcd(1,n) == 1:
        count += 1

print(count, [...])
