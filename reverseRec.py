def reverseA(l, low, high):
    if low > high:
        return
    l[low], l[high] = l[high], l[low]
    reverseA(l, low+1, high-1)


l = [1,2,3,4,5,6,7]
high = len(l)-1
reverseA(l, 0, high)
for a in l:
    print(a,end=" ")