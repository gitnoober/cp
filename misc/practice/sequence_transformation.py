import os
import sys
import collections
import itertools as it

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


# think about the edge cases

for _ in range(int(input())):
    n = int(input())
    a = list(maps())
    z = collections.Counter(list((i for i, j in it.groupby(a))))
    z[a[0]] -= 1
    z[a[n - 1]] -= 1
    print(min(z.values()) + 1)
