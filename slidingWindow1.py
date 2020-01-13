def sWindow(l, k, n):
    max_sum = 0

    max_sum = sum(l[i] for i in range(k))

    curr_sum = max_sum
    for i in range(k, n):
        curr_sum -= l[i-k] + l[i]
        max_sum = max(max_sum, curr_sum)

    return max_sum


l = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
n = len(l)
print(sWindow(l, k, n))
