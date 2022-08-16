for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    l = 0
    arr = [0] * (k + 1)
    for i in range(n):
        if a[i] <= k:
            arr[l] = i + 1
            l += 1
    c = 0
    for i in range(k + 1):
        if arr[i] > k:
            c += 1
    print(c)
