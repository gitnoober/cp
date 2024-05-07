import os
import sys
import bisect as bs

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


# THINK ABOUT THE EDGE CASES ..........
p = int(input())
ans = []
pr = 1
for i in range(1, 12):
    pr *= i
    ans.append(pr)
cnt = 0
# print(ans)
while p:
    idx = max(0, bs.bisect_right(ans, p) - 1)
    cnt += 1
    p -= ans[idx]
print(cnt)
