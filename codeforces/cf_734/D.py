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

for _ in range(*maps()):
    n = [*maps()][0]
    C, ans = [collections.Counter(input().rstrip("\n")) for _ in range(n)], 0
    for ch in "abcde":
        v = sorted(
            [cnt[ch] + sum([-v for k, v in cnt.items() if k != ch]) for cnt in C]
        )[::-1]
        s = sum(v)
        while v and s <= 0:
            s -= v.pop()
        ans = max(ans, len(v))
    print(ans)
