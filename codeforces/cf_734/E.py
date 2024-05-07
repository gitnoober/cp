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
    n, m, kh = maps()
    kv, ok = n * m // 2 - kh, True
    if n & 1:
        kh -= m // 2
        if kh < 0:
            ok = False
    if m & 1:
        kv -= n // 2
        if kv < 0:
            ok = False
    print("NO") if kv & 1 or kh & 1 or not ok else print("YES")
