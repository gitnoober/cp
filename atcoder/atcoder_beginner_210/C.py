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
n, k = maps()
a = list(maps())
d = collections.defaultdict(int)
ans = 0
for i in range(k):
    d[a[i]] += 1
    if d[a[i]] == 1:
        ans += 1
# print(ans)
t = ans
idx = 0
for i in range(k, n):
    if d[a[idx]] == 1:
        t -= 1
    d[a[idx]] -= 1
    if d[a[i]] == 0:
        t += 1
    d[a[i]] += 1
    ans = max(ans, t)
    idx += 1
print(ans)
