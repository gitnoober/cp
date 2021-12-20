inf = float('inf')
import sys
import pprint
import logging
from logging import getLogger
import array
import collections
from heapq import heapify, heappush, heappop, nlargest
# sys.setrecursionlimit(10 ** 9)


def solve():
    n, k = maps()
    a = list(maps())

    def ok(m):
        s = 0
        for i in a:
            s += min(m, i)
        return s >= m * k

    l, h = 0, 10**18
    ans = -1
    while l <= h:
        m = (l + h) >> 1
        if ok(m):
            ans = m
            l = m + 1
        else:
            h = m - 1
    print(ans)


if __name__ == '__main__':
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

    solve()
