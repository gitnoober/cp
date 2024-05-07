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
def nxt(submask, ai):
    N = 30
    aib, bi, sb = format(ai, "b"), [], format(submask, "b")
    aib, sb = "0" * (N - len(aib)) + aib, "0" * (N - len(sb)) + sb
    for i in range(len(aib)):
        if sb[i] == "1":
            if aib[i] == "0":
                bi.append("1")
            else:
                bi.append("0")
        else:
            bi.append("0")
    bi = int("".join(bi), 2)
    sb = ai ^ bi
    return bi, sb


for _ in range(int(input())):
    n = int(input())
    a = list(maps())
    prev = 0
    for i in range(n):
        ap = (prev | a[i]) - a[i]
        prev = ap | a[i]
        print(ap, end=" ")
    print()
