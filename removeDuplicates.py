def duplicates(arr):
    n = len(arr)
    s = set()

    for i in arr:
        s.add(i)

    return list(s)



lis = [1, 2, 5, 1, 7, 2, 4, 2]
print(duplicates(lis))