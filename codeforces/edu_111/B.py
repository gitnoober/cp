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
    n, a, b = maps()
    s = input().rstrip("\n")
    if b > 0:
        print((a + b) * n)
    else:
        diff = s.count("10") + s.count("01") + 1
        print(a * n + b * (diff // 2 + 1))
# didn't take care of the length one diff , forgot that there will be different answer for length of diff 1 and greater than 1
