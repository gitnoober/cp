inf = float("inf")
import sys
import pprint
import logging
from logging import getLogger
import array

sys.setrecursionlimit(10**7)


def input():
    return sys.stdin.readline().rstrip("\r\n")


def maps():
    return [int(i) for i in input().split()]


logging.basicConfig(
    format="%(message)s",
    level=logging.WARNING,
)
logger = getLogger(__name__)
logger.setLevel(logging.INFO)


def debug(msg, *args):
    logger.info(f"{msg}={pprint.pformat(args)}")


mod = 998244353
N = 10**6
gr = [[] for _ in range(N)]
vis = array.array("b", [False] * N)


def dfs(u):
    global p, path
    vis[u] = True
    p += len(gr[u])
    path += 1

    for v in gr[u]:
        if not vis[v]:
            dfs(v)


n, m = maps()
for _ in range(m):
    u, v = maps()
    gr[u].append(v)
    gr[v].append(u)


ans = 1
for i in range(1, n + 1):
    if not vis[i]:
        p = path = 0
        dfs(i)
        if path * 2 == p:  # counting edges twice
            ans *= 2
            ans %= mod
        else:
            ans = 0
print(ans)
