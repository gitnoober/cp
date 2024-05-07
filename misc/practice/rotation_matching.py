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


(n,) = maps()
a = [*maps()]
b = [*maps()]
d, cnt = {b[i]: i for i in range(n)}, {}
for i in range(n):
    x = d[a[i]] - i
    if x < 0:
        x += n
    # convert this into left shift although right shift would be lesser but it's the same thing
    # 1 right shift is n-1 left shift and vice-versa
    cnt[x] = cnt.get(x, 0) + 1
print(max(cnt[v] for v in cnt))
