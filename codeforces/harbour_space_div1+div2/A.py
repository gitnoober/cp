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
def s(x):
    return sum([int(i) for i in str(x)])


def func(n):
    ans = 0
    for i in range(1, n + 1):
        if s(i + 1) < s(i):
            ans += 1
    return ans


for _ in range(*maps()):
    n = int(input())
    t = n // 10 + (1 if n % 10 == 9 else 0)
    print(t)
