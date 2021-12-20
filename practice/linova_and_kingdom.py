
import sys
import pprint
import logging
from logging import getLogger
def input(): return sys.stdin.readline().rstrip("\r\n")


logging.basicConfig(format="%(message)s", level=logging.WARNING,)
logger = getLogger(__name__)
logger.setLevel(logging.INFO)


def debug(msg, *args):
    logger.info(f'{msg}={pprint.pformat(args)}')

# 30 MINUTES ATLEAST !!!!

###################################################################################################################


maxn = int(2e5 + 10)

gr = [[] for _ in range(maxn)]
vis = [False] * maxn
dist = [-1] * maxn
dp = {i: 0 for i in range(maxn)}


def build():
    for i in range(n - 1):
        u, v = map(lambda x: int(x) - 1, input().split())
        gr[u].append(v)
        gr[v].append(u)


def BFS():
    Q = [(0, 0)]
    dist[0] = 0
    vis[0] = True

    for dis, v in Q:
        for w in gr[v]:
            if not vis[w]:
                vis[w] = True
                dist[w] = dis + 1
                Q.append((dist[w], w))


def dfs(start=0):

    finished = [False] * n

    stack = [start]
    while stack:
        start = stack[-1]

        # push unvisited children into stack
        if not vis[start]:
            vis[start] = True
            for child in gr[start]:
                if not vis[child]:
                    stack.append(child)

        else:
            stack.pop()

            # base case
            dp[start] += 1

            # update with finished children
            for child in gr[start]:
                if finished[child]:
                    dp[start] += dp[child]

            finished[start] = True


if __name__ == '__main__':
    n, k = map(int, input().split())
    build()
    BFS()
    for i in range(n):
        vis[i] = False
    dfs()

    f = [0] * n
    for i in range(n):
        f[i] = dist[i] - (dp[i] - 1)
    f.sort()

    ans = 0
    for i in range(n - 1, n - k - 1, - 1):
        ans += f[i]
    print(ans)
