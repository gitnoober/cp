inf = float("inf")
import sys
import pprint
import logging
from logging import getLogger

# sys.setrecursionlimit(10 ** 9)


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


# import dataclasses


(n,) = maps()
inn = [[] for _ in range(n)]

for i in range(n - 1):
    u, v = map(lambda x: int(x) - 1, input().split())
    inn[u].append(i)
    inn[v].append(i)
inn.sort(key=lambda x: -len(x))
vis = [False] * n
mx = 0
ans = [0] * (n - 1)
for i in inn:
    for j in i:
        if not vis[j]:
            ans[j] = mx
            mx += 1
            vis[j] = True


# debug("inn", inn)
# debug("ans", ans)
print(*ans)
