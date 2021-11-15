inf = float('inf')
import sys
import pprint
import logging
from logging import getLogger
import array
import collections

# sys.setrecursionlimit(10 ** 9)

def input(): return sys.stdin.readline().rstrip("\r\n")

def maps(): return [int(i) for i in input().split()]


logging.basicConfig(
    format="%(message)s",
    level=logging.WARNING,
)
logger = getLogger(__name__)
logger.setLevel(logging.INFO)


def debug(msg, *args):
    logger.info(f'{msg}={pprint.pformat(args)}')


for _ in range(*maps()):
    n, m = maps()
    s = input()
    dic = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    l = r = u = d = 0
    x = y = 0
    for i in s:
        dx, dy = dic[i]
        x, y = x + dx, y + dy

        if ((x < u or x > d) and d - u + 1 == n) or ((y > r or y < l) and r - l + 1 == m):
            break

        l = min(l, y)
        r = max(r, y)
        u = min(u, x)
        d = max(d, x)
    print(-u + 1, -l + 1)
