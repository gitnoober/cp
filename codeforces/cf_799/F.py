for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ok = False
    i, j, k = 0, 1, n - 1
    while i < j < k:
        s = a[i] + a[j] + a[k]
        if str(s)[-1] == "3":
            ok = True
            break
