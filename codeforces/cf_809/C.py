N = int(input())
for _ in range(N):
    n = int(input())
    a = list(map(int, input().split()))
    if n % 2:
        ans = 0

        for i in range(1, n - 1, 2):
            ans += max(max(a[i - 1], a[i + 1]) + 1 - a[i], 0)
        print(ans)
    else:
        ans = float("inf")
        j = 1
        pr1 = [0] * n
        pr2 = [0] * n
        for i in range(1, n - 1, 2):
            r = max(max(a[i - 1], a[i + 1]) + 1 - a[i], 0)
            pr1[j] = pr1[j - 1] + r
            j += 1
        j = 1
        for i in range(2, n - 1, 2):
            r = max(max(a[i - 1], a[i + 1]) + 1 - a[i], 0)
            pr2[j] = pr2[j - 1] + r
            j += 1

        for i in range(n // 2):
            ans = min(ans, pr1[i] + pr2[n // 2 - 1] - pr2[i])
        print(ans)
