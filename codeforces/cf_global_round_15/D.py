import os
import sys
import math as mt

maxx, localsys, mod = 1 << 60, 0, int(1e9 + 7)


def nCr(n, r):
    return reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)


def ceil(n, x):
    return (n + x - 1) // x


def lcm(x, y):
    return x * y // mt.gcd(x, y)


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


#   THINK ABOUT THE EDGE CASES ..........

#   DON'T SUBMIT UNLESS YOU ARE ABSOLUTELY SURE !!!!!


def recur(arr, pos=0, sum_=0):
    if pos == n:
        return False
    if arr[pos] == sum_:
        return True
    return any(recur(arr, pos + 1, sum_ + x) for x in [0, -arr[pos], arr[pos]])


for _ in range(*maps()):
    (n,) = maps()
    a = [*maps()]
    print(["YES", "NO"][recur(a) ^ 1])
