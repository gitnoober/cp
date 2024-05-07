import sys


def input():
    return sys.stdin.readline().rstrip("\r\n")


def maps():
    return [int(i) for i in input().split()]


mod = 998244353
(n,) = maps()
s = input()
dp = [[[0 for _ in range(10)] for _ in range(1 << 10)] for _ in range(n + 1)]

for i in range(1, n + 1):
    # till i-1 is already calculated
    ch = ord(s[i - 1]) - 65

    # for every set j
    for j in range(1024):
        for k in range(10):
            dp[i][j][k] = dp[i - 1][j][k]  # does not participate in the contest
            if k == ch:
                dp[i][j][k] += dp[i - 1][j][
                    k
                ]  # if there is already a ch then add it to the subsequences that ends with ch
                dp[i][j][k] %= mod

    # for every set j
    for j in range(1024):
        if j & (
            1 << ch
        ):  # if set then the sequence already has a ch and it has been dealt with
            continue
        for k in range(10):
            dp[i][j | (1 << ch)][ch] += dp[i - 1][j][
                k
            ]  # if ch is the first occurence then add it to all the other subsequences i.e add ch to all the other previous subsequences
            dp[i][j | (1 << ch)][ch] %= mod

    dp[i][1 << ch][
        ch
    ] += 1  # making a new subsequence with the ch (inclusion third case) , first contest he participated is the ith one.
    dp[i][1 << ch][ch] %= mod


ans = 0
for j in range(1024):
    for k in range(10):
        ans += dp[n][j][k]
        ans %= mod
print(ans)
