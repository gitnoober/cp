import os
import sys

maxx, localsys, mod = float("inf"), 0, int(1e9 + 7)
nCr, ceil = (
    lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r),
    lambda n, x: (n + x - 1) // x,
)
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


def ok(arr, pos):
    cur = arr[pos]
    for i in range(n):
        if i == pos:
            continue
        if cur < a[i]:
            return False
        cur += a[i]
    return True


for _ in range(int(input())):
    n = int(input())
    a = list(maps())
    b = a[:]
    a.sort()
    ans, l, h = [], -1, n - 1
    while h - l > 1:
        m = (l + h) // 2
        l, h = (l, m) if ok(a, m) else (m, h)
    ans = [i + 1 for i in range(n) if b[i] >= a[h]]
    print(len(ans))
    print(*ans)
