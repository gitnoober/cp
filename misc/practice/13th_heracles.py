import os
import sys
import collections as c

maxx, localsys, mod = float("inf"), 0, int(1e9 + 7)
def nCr(n, r):
    return reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
def ceil(n, x):
    return (n + x - 1) // x
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


for _ in range(int(input())):
    n = int(input())
    a = list(maps())
    d = c.defaultdict(list)
    ans, ar, cc = [sum(a)], [], [0] * n
    for i in range(n - 1):
        u, v = maps()
        cc[u - 1] += 1
        cc[v - 1] += 1
    for i in range(n):
        ar.extend([a[i]] * (cc[i] - 1))
    ar.sort(reverse=True)
    # print(ar)
    for i in range(n - 2):
        ans.append(ans[-1] + ar[i])
    print(*ans)
