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

for _ in range(*maps()):
    s1 = input().rstrip("\n")
    s2 = input().rstrip("\n")
    n1, n2 = len(s1), len(s2)
    ok = False
    for i in range(n1):
        x = s1[:i] + s1[i::-1]
        if s2 in x:
            ok = True
    print(["NO", "YES"][ok])
