import os
import sys
import collections

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
    n, m = maps()
    d = collections.defaultdict(lambda: [0] * 26)
    for _ in range(n):
        s = input().rstrip("\n")
        for i in range(m):
            d[i][ord(s[i]) - 97] += 1
    for _ in range(n - 1):
        s = input().rstrip()
        for i in range(m):
            d[i][ord(s[i]) - 97] -= 1
    sx = ""
    for i in range(m):
        for j in range(26):
            if d[i][j]:
                print(chr(j + 97), end="")
                break
    print()
