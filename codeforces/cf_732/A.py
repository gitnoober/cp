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
    b = list(maps())
    l1, l2 = [], []
    for i, (a, b) in enumerate(zip(a, b)):
        if a > b:
            l1 += [i + 1] * (a - b)
        else:
            l2 += [i + 1] * (b - a)
    if len(l1) == len(l2):
        print(len(l1))
        [print(i, j) for i, j in zip(l1, l2)]
    else:
        print(-1)
