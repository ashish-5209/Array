def bonacci(k, n):

    if n < k:
        return 0
    if n == k:
        return 1
    x = k
    res = 0
    while x > 0:
        res += bonacci(k,n-x)
        x -= 1

    return res

def efficientSol(k,n):
    a = [0 for i in range(n)]
    a[k] = 1
    a[k-1] = 1

    for i in range(k+1,n):
        a[i] = 2*a[i-1] - a[i-k-1]

    return a[n-1]


print(bonacci(5,15))
print(efficientSol(5,15))