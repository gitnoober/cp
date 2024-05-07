inf = float("inf")
import sys
import pprint
import logging
from logging import getLogger

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


def A():
    s = input()
    i = 0
    while i < len(s) and s[i] != ".":
        i += 1
    if int(s[i + 1]) >= 5:
        print(int(s[:i]) + 1)
    else:
        print(int(s[:i]))


def B():
    (n,) = maps()
    se = set()
    for i in range(n):
        x = [*maps()]
        se.add(tuple(x[1:]))
    print(len(se))


def C():
    (n,) = maps()
    # learn nth move
    gr = [[] for _ in range(n + 1)]
    d = {}
    learnt = [False] * (n + 1)
    for i in range(n):
        x = list(maps())
        d[i + 1] = x[0]
        for j in x[2:]:
            gr[i + 1].append(j)

    debug("gr", gr)
    ans = 0

    def dfs(u):
        nonlocal ans
        learnt[u] = True
        ans += d[u]

        for v in gr[u]:
            if not learnt[v]:
                dfs(v)

    dfs(n)
    print(ans)
    # print(gr)


C()
