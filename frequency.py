from collections import defaultdict
arr = [9,9,9,2,5]
m = 0
d = defaultdict(lambda:0)
for i in arr:
    d[i] += 1
    m = max(m, d[i])

print(m, [...])
