def leaders(l,n):
    arr = []
    max = l[n]
    arr.append(max)
    print(max,end=" ")

    for i in range(n-1, -1, -1):
        if l[i] > max:
            arr.insert(0, l[i])
            max = l[i]
            print(max,end=" ")
    print()
    for x in arr:
        print(x,end=" ")



l = [16,17,4,3,5,2]
n = len(l)-1
leaders(l,n)
