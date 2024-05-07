import sys


def input():
    return sys.stdin.readline().rstrip("\r\n")


def maps():
    return [int(i) for i in input().split()]


def A():
    a, b = maps()
    print((a - b) / 3 + b)


def B():
    t = ["H", "2B", "HR", "3B"]
    ok = [False] * 4
    for _ in range(4):
        s = input()
        for i in range(4):
            if t[i] == s:
                ok[i] = True

    print("Yes" if all(ok) else "No")


def C():
    s = input()
    t = "chokudai"
    n = len(s)
    m = len(t)
    mod = int(1e9 + 7)

    dp = [[0 for _ in range(m + 1)] for __ in range(n + 1)]

    dp[0][0] = 1

    for i in range(1, n + 1):
        dp[i][0] = 1
        for j in range(1, m + 1):

            dp[i][j] = dp[i - 1][j]

            if s[i - 1] == t[j - 1]:
                dp[i][j] += dp[i - 1][j - 1]

            dp[i][j] %= mod

    print(dp[n][m])


C()
