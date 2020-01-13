def maxDiff(arr, n):
    res = arr[1] - arr[0]
    minVal = arr[0]

    for i in range(1, n):
        res = max(res, arr[i] - minVal)
        minVal = min(minVal, arr[i])

    return res

arr = [2,3,10,6,4,8,1]
print(maxDiff(arr, len(arr)))
