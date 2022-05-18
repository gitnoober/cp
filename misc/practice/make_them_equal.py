N = 1001
dp = {i: float("inf") for i in range(N)}
dp[1] = 0

for i in range(1, N):
    for x in range(1, i + 1):
        j = i + (i // x)
        if j < N:
            dp[j] = min(dp[j], dp[i] + 1)


for _ in range(int(input())):
    n, k = map(int, input().split())
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    sum_ = 0
    for x in b:
        sum_ += dp[x]
    k = min(k, sum_)

    kdp = [0] * (k + 1)
    for i in range(n):
        for j in range(k - dp[b[i]], -1, -1):
            kdp[j + dp[b[i]]] = max(kdp[j + dp[b[i]]], c[i] + kdp[j])

    print(max(kdp))
