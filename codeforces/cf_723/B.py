# If God , doesn't know chuck does

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


# you can use lambda in list comprehension and apply them.

[
    (lambda n: print("YES" if n >= (n % 11) * 111 else "NO"))(int(input()))
    for _ in range(int(input()))
]

# you can also use a theorem where  every number after 1099 is a combinations of sums of 11 and 111
