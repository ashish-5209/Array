def equilibrium(arr):

    n = len(arr)

    s = sum(arr)

    l_sum = 0

    for i in range(n):
        s -= arr[i]

        if s == l_sum:
            return True
        l_sum += arr[i]

    return False


arr = [-7, 1, 5, 2, -4, 3, 0]
print(equilibrium(arr))