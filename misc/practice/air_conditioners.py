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

for _ in range(int(input())):
    input()
    n, k = maps()
    a = list(maps())
    t, c = list(maps()), [maxx] * n
    for i in range(k):
        c[a[i] - 1] = t[i]  # with t[j] + abs(a[j] -i) --> i == a[j]
    for i in range(1, n):
        c[i] = min(c[i], c[i - 1] + 1)
    for i in range(n - 1, 0, -1):
        c[i - 1] = min(c[i] + 1, c[i - 1])
    [print(i, end=" ") for i in c]
    print()
