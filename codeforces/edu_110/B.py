import os
import sys
import math

maxx, localsys, mod = float("inf"), 0, int(1e9 + 7)
def nCr(n, r):
    return reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
def ceil(n, x):
    return (n + x - 1) // x
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


for _ in range(int(input())):
    n = int(input())
    arr = list(maps())
    ap = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                if math.gcd(arr[i], 2 * arr[j]) > 1:
                    ap += 1
                elif math.gcd(arr[j], 2 * arr[i]) > 1:
                    ap += 1
    print(ap // 2)
