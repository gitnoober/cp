import os
import sys

maxx, localsys, mod = 1 << 60, 0, int(1e9 + 7)


def nCr(n, r):
    return reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)


def ceil(n, x):
    return (n + x - 1) // x


osi, oso = (
    "/home/priyanshu/Documents/cp/input.txt",
    "/home/priyanshu/Documents/cp/output.txt",
)
if os.path.exists(osi):
    sys.stdin = open(osi, "r")
    sys.stdout = open(oso, "w")

input = sys.stdin.readline


def maps():
    return map(int, input().split())


# THINK ABOUT THE EDGE CASES ..........


def func(word1, word2):
    n1, n2 = len(word1), len(word2)
    dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
    # dp state ( dp[i][j]) means word1[....:i] == word2[....j]
    for i in range(n2 + 1):
        dp[0][i] = i
    for i in range(n1 + 1):
        dp[i][0] = i
    # incase of length of the other string being 0
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
    return dp[n1][n2]


word1 = ""
word2 = "a"
print(func(word1, word2))
