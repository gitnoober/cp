import os
import sys
import math as mt
import operator as op
import functools as fn

maxx, localsys, mod = 1 << 60, 0, int(1e9 + 7)


def nCr(n, r):
    return fn.reduce(op.mul, range(n - r + 1, n + 1), 1) // mt.factorial(r)


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

for _ in range(*maps()):
    (n,) = maps()
    a = [*maps()]
    d = {a[i]: i for i in range(n)}
    ans = "YES"
    if d[1] == n - 1 or d[n] == 0 or a[0] > a[n - 1]:
        ans = "NO"
    print(ans)
"""
if a[0] > a[n-1] then the only way we can remove a[1] is by pairing it up with a greater element , and
therefore te leftmost element can only increase and not decrease(leftmost element is non-decreasing).

if a[0] < a[n-1] , then find the smallest index r where a[0] < a[r] then elements b/w 0 and r are less than a[0] and
a[r] and thus trimming the whole segment to just a[0] , keep repeating this algorithm and at the end a[0] < a[n-1]
will be left and thus making the array good.
"""
