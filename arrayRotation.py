def reverseA(l, low, high):
    if low > high:
        return
    l[low], l[high] = l[high], l[low]
    reverseA(l, low+1, high-1)



def rotateArray(l, d, high):
    reverseA(l, 0, d-1)
    reverseA(l, d, high)
    reverseA(l, 0, high)


l = [1,2,3,4,5,6,7]
high = len(l)-1
rotateArray(l, 2, high)
for a in l:
    print(a,end=" ")