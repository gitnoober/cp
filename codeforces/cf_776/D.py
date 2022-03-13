from collections import deque

# a = deque([1, 2, 3])
# a.rotate(-1)
# print(a)


for _ in range(int(input())):
    n = int(input())
    a = deque(map(int, input().split()))
    ans = [0 for i in range(n)]
    arr = [i + 1 for i in range(n)]
    i = n - 1
    while a:
        x = arr[-1]
        idx = a.index(x) + 1
        if idx == x:
            idx = 0

        # print(a, arr, "before")
        a.rotate(-idx)
        # print(a, arr, "after", idx)
        a.pop()
        arr.pop()
        ans[i] = idx
        i -= 1
    print(*ans)
