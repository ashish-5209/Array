from math import sqrt, floor

def isPrime(n):
    arr = [1]*(n+1)
    arr[0] = 0
    arr[1] = 0

    for i in range(2,floor(sqrt(n)+1)):

        if arr[i] == 1:
            j = 2
            while i*j <= n:
                arr[i*j] = 0
                j += 1


    for i in range(n+1):
        if arr[i] == 1:
            print(i, end=' ')

isPrime(50)
