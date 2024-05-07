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


# THINK ABOUT THE EDGE CASES ..........
n, k = maps()
a = list(maps())
common = k // n
left = k - common * n
d = {i: a[i] for i in range(n)}
a.sort()
ok = True
if n == left:
    ok = False
for i in range(n):
    if ok:
        # a[i] < a[left]
        if d[i] < a[left]:
            print(common + 1)
        else:
            print(common)
    else:
        if d[i] <= a[left]:
            print(common + 1)
        else:
            print(common)
