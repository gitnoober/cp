import os
import sys

maxx, localsys, mod = float("inf"), 0, int(1e9 + 7)
def nCr(n, r):
    return reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
def ceil(n, x):
    return (n + x - 1) // x
osi, oso = (
    "/home/priyanshu/Documents/sublimetextproject/input.txt",
    "/home/priyanshu/Documents/sublimetextproject/output.txt",
)
if os.path.exists(osi):
    sys.stdin = open(osi, "r")
    sys.stdout = open(oso, "w")

input = sys.stdin.readline


def maps():
    return map(int, input().split())


"""
dp(i,ilast) -- is the number of substrings till ith position when the ilast = 1 or 0
the substring has to be unstable so ,'1' and 1(every individual character is an unstable substring) + the # of substring where the last character is '0'
and vice-versa.

"""
for _ in range(int(input())):
    s = input().rstrip("\n")
    n = len(s)
    dp1, dp2 = [0] * n, [0] * n
    if s[0] != "1":
        dp1[0] = 1
    if s[0] != "0":
        dp2[0] = 1
    for i in range(1, n):
        if s[i] != "1":
            dp1[i] = 1 + dp2[i - 1]
        if s[i] != "0":
            dp2[i] = 1 + dp1[i - 1]

    print(sum(max(dp1[i], dp2[i]) for i in range(n)))
