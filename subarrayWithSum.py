def naiveSoln(arr,x):

    n = len(arr)

    for i in range(n):
        curr_sum = 0
        for j in range(i,n):
            curr_sum += arr[j]

            if curr_sum == x:
                return True

    return False

def efficientSol(arr,x):
    curr_sum = arr[0]
    s = 0
    n = len(arr)

    for e in range(1, n):
        while(curr_sum > x and s < e):
            curr_sum -= arr[s]
            s += 1

        if curr_sum == x:
            return True

        curr_sum += arr[e]

    return curr_sum == x



arr = [1,8,30,5,20,7]
print(naiveSoln(arr,32))
print(efficientSol(arr,32))