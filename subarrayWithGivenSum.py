def naiveSoln(arr,k,x):

    n = len(arr)
    for i in range(n-k+1):
        curr_sum = 0
        for j in range(i,k+i):
            curr_sum += arr[j]

        if curr_sum == x:
            return True

    return False


def efficientSol(arr,k,x):

    n = len(arr)
    curr_sum = 0
    for i in range(k):
        curr_sum += arr[i]

    if curr_sum == x:
        return True

    for i in range(k,n):
        curr_sum += arr[i] - arr[i-k]

        if curr_sum == x:
            return True

    return False



arr = [1,8,30,-5,20,7]
k=3
print(naiveSoln(arr,k,22))
print(efficientSol(arr,k,48))