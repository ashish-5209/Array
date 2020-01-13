def cylinder(l, n):
    x = l[n-1]
    for i in range(n-1, 0, -1):
        l[i] = l[i-1]

    l[0] = x


l = [1,2,3,4,5]
cylinder(l,len(l))
for i in l:
    print(i,end=" ")