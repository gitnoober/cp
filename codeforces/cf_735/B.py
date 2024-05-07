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


for _ in range(*maps()):
    n, k = maps()
    a = [*maps()]
    x = max(0, n - 2 * k)
    ans = -maxx
    for i in range(x, n):
        for j in range(i + 1, n):
            f = (i + 1) * (j + 1)
            ans = max(ans, f - k * (a[i] | a[j]))
    print(ans)
