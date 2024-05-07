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


for _ in range(int(input())):
    n = int(input())
    a = sorted(maps())
    idx = min(range(n - 1), key=lambda x: a[x + 1] - a[x])
    print(*[a[idx]] + a[idx + 2 :] + a[:idx] + [a[idx + 1]])
