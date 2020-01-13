import sys
def maxDif(arr, n):
    m = -sys.maxsize - 1

    for i in range(n):
        for j in range(i+1, n):
            c = arr[j] - arr[i]
            m = max(m, c)

    return m

arr = [2,3,10,6,4,8,1]
print(maxDif(arr, len(arr)))
