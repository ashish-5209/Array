def naiveSoln(arr,k):
    max_sum = 0
    n = len(arr)
    for i in range(n-k+1):
        curr_sum = 0
        for j in range(i,i+k):
            curr_sum += arr[j]

        max_sum = max(curr_sum,max_sum)

    return max_sum


def efficientSol(arr,k):

    curr_sum = 0
    n = len(arr)

    for i in range(k):
        curr_sum += arr[i]

    max_sum = curr_sum

    for i in range(k,n):
        curr_sum += arr[i] - arr[i-k]

        max_sum = max(max_sum,curr_sum)

    return max_sum


arr = [1,8,30,-5,20,7]
k=3
print(naiveSoln(arr,k))
print(efficientSol(arr,k))