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


def func():
    u, v = maps()
    if v == 0:
        print(0 if not u else -1)
        return

    if u == v:
        print(1, '\n', v)
        return

    if (u > v) or (u & 1 != v & 1):
        print(-1)
        return

    x = v - u
    ans = [u] if u else []

    if (x // 2) ^ (v - (x // 2)) == u:
        print(2, '\n', x // 2, v - (x // 2))
        return

    ans = [u, x // 2, x // 2]
    print(len(ans), '\n', *ans)


func()
