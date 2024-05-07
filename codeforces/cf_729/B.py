import os
import sys
import math

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
    n, a, b = maps()
    power = 1 if a == 1 else int(math.log(n, a) + 1)
    ok = False
    for i in range(power + 1):
        t = n - pow(a, i)
        if t % b == 0 and t >= 0:
            ok = True
            break
    print("Yes" if ok else "No")
