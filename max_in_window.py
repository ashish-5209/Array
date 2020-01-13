def max_window(arr, n, k):
    st = []
    res = []
    for i in range(k):
        if len(st) == 0:
            st.append(i)
        else:
            while len(st) != 0 and arr[st[-1]] <= arr[i]:
                st.pop()
            st.append(i)
    res.append(arr[st[0]])

    for i in range(k, n):
        while st[0] <= (i-k):
            st.pop(0)
        while len(st) != 0 and arr[st[-1]] <= arr[i]:
            st.pop()
        st.append(i)
        res.append(arr[st[0]])

    return res

arr = [1,3,-1,-3,5,3,6,7]
k = 3
n = len(arr)

print(max_window(arr, n, k))
