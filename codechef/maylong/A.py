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
for _ in range(int(input())):
    n = int(input())
    print(ceil(2**n - 1, 2))
