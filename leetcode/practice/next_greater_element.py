def func(arr):
    n = len(arr)
    st = []
    ans = []
    for i in range(n - 1, -1, -1):
        if st:
            while st and st[-1] <= arr[i]:
                st.pop()

        ans.append(-1 if not st else st[-1])
        st.append(arr[i])

    return ans[::-1]


arr = [11, 13, 21, 3]
ans = func(arr)
print(ans)
