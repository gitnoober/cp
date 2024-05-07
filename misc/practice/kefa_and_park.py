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
from functools import reduce


def maps():
    return map(int, input().split())


# THINK ABOUT THE EDGE CASES ..........


def bfs(a, k, vis, gr):
    q, i, ans = [(0, 0)], 0, 0
    while i < len(q):
        idx, acc = q[i]
        vis[idx] = ok = True
        if acc + a[idx] <= k:
            for v in gr[idx]:
                if not vis[v]:
                    ok = False
                    q.append((v, a[idx] * (acc + a[idx])))  # consecutive 1's !!!
        else:
            ok = False
        if ok:
            ans += 1
        i += 1
    return ans


n, k = maps()
a, gr, vis = list(maps()), [[] for _ in range(n)], [False] * n
for _ in range(n - 1):
    u, v = maps()
    gr[u - 1].append(v - 1)
    gr[v - 1].append(u - 1)
print(bfs(a, k, vis, gr))
