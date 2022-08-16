from math import ceil


def func(n, l, r):
    a = [-1] * n
    for i in range(1, n + 1):
        lo = l // i
        hi = r // i
        lo *= i
        hi *= i

        if hi < l or lo > r:
            return (False, a)
        a[i - 1] = hi
    return (True, a)


N = int(input())
for _ in range(N):
    n, l, r = map(int, input().split())
    if n > 2 * (r - l + 1):
        print("NO")
        continue
    arr = [-1] * n
    arr[0] = l
    ok = True
    for i in range(1, n):
        x = ceil(l / (i + 1)) * (i + 1)
        if x <= r and x >= l:
            arr[i] = x
        else:
            ok = False
    # # print(arr)
    # ok, arr = func(n, l, r)
    print(["NO", "YES"][ok])
    if ok:
        print(*arr)
