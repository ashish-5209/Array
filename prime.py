def isPrime(N):
    # Your code here
    if N == 2 or N == 3:
        return True

    n1 = (N + 1) / 6
    n2 = (N - 1) / 6

    if n1 == int(n1):
        return True
    elif n2 == int(n2):
        return True
    else:
        return False


print(isPrime(5))
print(isPrime(7))
print(isPrime(23))
print(isPrime(161))
print(isPrime(44))