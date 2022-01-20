
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
from bisect import bisect_left
from itertools import accumulate


def accurate(x, y):
    val = x // y
    while val * y > x:
        val -= 1

    return val


def solve():
    n, k = inp()
    a = sorted(inp())
    pr = list(accumulate(a))
    ans = float('inf')

    for y in range(n):
        x = a[0] - accurate(k - pr[n - y - 1] + a[0], y + 1)
        ans = min(ans, y + max(x, 0))
    print(ans)


if __name__ == '__main__':
    multi = True
    t = 1

    def inp(): return map(int, input().split())

    if multi:
        t = int(input())

    while t:
        t -= 1
        solve()
