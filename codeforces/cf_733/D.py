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
    n = int(input())
    a = list(maps())
    ok = [0] * n
    k = 0
    arr = [0] * n
    for i in range(n):
        if ok[a[i] - 1] == 0:
            k += 1
            ok[a[i] - 1] = 1
            arr[i] = 1
    idx = 0
    for i in range(n):
        if arr[i] == 0:
            while idx < n and ok[idx]:
                idx += 1
            a[i] = idx + 1
    d = {a[i]: i for i in range(n)}
    for i in range(n):
        if a[i] == i + 1:
            a[i + 1]
