def reverseA(l):
    i = 0
    h = len(l)-1
    while i < h:
        l[i], l[h] = l[h], l[i]
        i += 1
        h -= 1

    for a in l:
        print(a, end=" ")


l = [1, 2, 3, 4, 5]
reverseA(l)