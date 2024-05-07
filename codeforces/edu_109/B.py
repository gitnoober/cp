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


# [print(Fraction(int(input()), 100).denominator) for _ in range(int(input()))] --- Solution to Problem A

for _ in range(int(input())):
    n = int(input())
    a = list(maps())
    b = sorted(a)
    s = []
    for idx in enumerate(zip(a, b)):
        if idx[1][0] != idx[1][1]:
            s.append(idx[0])
    if not s:
        print(0)
    elif a[0] == 1 or a[-1] == n:
        print(1)
    else:
        A = sorted(a[: n - 1]) + [a[-1]]
        B = [a[0]] + sorted(a[1:n])
        if sorted(A) == A or sorted(B) == B:
            print(1)
        A = [A[0]] + sorted(A[1:n])
        B = sorted(B[: n - 1]) + [B[-1]]
        if sorted(A) == A or sorted(B) == B:
            print(2)
        else:
            print(3)
