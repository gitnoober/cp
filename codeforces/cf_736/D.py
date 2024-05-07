import os
import sys
import math as mt

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


#   THINK ABOUT THE EDGE CASES ..........

#   DON'T SUBMIT UNLESS YOU ARE ABSOLUTELY SURE !!!!!
gcd = mt.gcd


def query(l, r):
    j = log[r - l + 1]
    return gcd(st[l][j], st[r - (1 << j) + 1][j])


for _ in range(*maps()):
    (n,) = maps()
    a, k = [*maps()], mt.floor(mt.log2(n))
    st = [[0 for _ in range(k + 1)] for __ in range(n)]

    for i in range(1, n):
        st[i][0] = abs(a[i] - a[i - 1])

    log = [0] * n + [0]
    log[0] = 1
    for i in range(2, n + 1):
        log[i] = log[i // 2] + 1

    for j in range(1, k + 1):
        i = 1
        while i + (1 << j) <= n:
            st[i][j] = gcd(st[i][j - 1], st[i + (1 << (j - 1))][j - 1])
            i += 1

    ans = j = 1
    for i in range(1, n):
        while j <= i and query(j, i) == 1:
            j += 1
        ans = max(ans, i - j + 2)

    print(ans)
