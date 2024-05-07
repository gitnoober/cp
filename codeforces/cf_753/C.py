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


for _ in range(*maps()):
    (n,) = maps()
    a = list(maps())
    if n == 1:
        print(a[0])
        continue
    a.sort()
    mi = a[0]
    curr = a[0]
    for i in range(1, n):
        mi = max(mi, a[i] - curr)
        curr += a[i] - curr
    print(mi)
