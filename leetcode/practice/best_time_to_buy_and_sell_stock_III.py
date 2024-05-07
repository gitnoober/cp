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


def func(prices):
    n = len(prices)
    A = []
    mi, ansmx = prices[0], 0
    for i in range(n):
        mi = min(mi, prices[i])
        ansmx = max(ansmx, prices[i] - mi)
        A.append(ansmx)

    mx = prices[-1]
    ansmx = 0
    ANS = 0
    for i in range(n - 1, -1, -1):
        mx = max(mx, prices[i])
        ansmx = max(ansmx, mx - prices[i])
        ANS = max(ANS, A[i] + ansmx)
    return ANS


prices = [2, 1, 2, 0, 1]
print(func(prices))
