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


def solve():
    n, k = maps()
    a = list(10**i for i in maps())
    b = [0] * n
    req = k + 1
    for i in range(n - 1):
        b[i] = (a[i + 1] // a[i]) - 1  # these are the values I can use
    b[n - 1] = inf  # use as many values you want of a[n-1] denomination
    ans = 0

    for i in range(n):
        use_here = min(b[i], req)
        req -= use_here
        ans += use_here * a[i]

    print(ans)


(tc,) = maps()
while tc:
    tc -= 1
    solve()
