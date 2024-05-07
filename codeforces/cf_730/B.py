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
    s = sum(a)
    if s % n:
        avg = s // n
        x = (
            s - avg * n
        )  # <-- tot diff. left which will be further distributed into n and the abs(avg - left) will only be done with numbers with whome the left part was not distributed
        print(x * (n - x))
    else:
        print(0)
