import os
import sys

maxx, localsys, mod = float("inf"), 0, int(1e9 + 7)
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


def rel(a, b):
    return abs(a - b) / max(1, abs(b))


for _ in range(int(input())):
    x, y, ans = [], [], 0
    for i in range(2 * int(input())):
        u, v = maps()
        y.append(v) if not u else x.append(u)
    print(
        sum(
            ((i * i) + (j * j)) ** 0.5
            for i, j in zip(sorted(x, key=abs), sorted(y, key=abs))
        )
    )
