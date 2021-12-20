
# DON'T SUBMIT UNLESS YOU'RE ABSOLUTELY SURE OR ATLEAST 70 % SURE !!!

import array
import bisect
import collections
import heapq
import io
import logging
import os
import pprint
import sys

from logging import getLogger

# sys.setrecursionlimit(10 ** 9)

inf = float('inf')


def solve():

    def chk(x):
        c = 0
        for i in range(n):
            if x - 1 - c <= a[i] and c <= b[i]:
                c += 1
        return c >= x

    n, = linp()
    a, b = [0] * n, [0] * n

    for i in range(n):
        a[i], b[i] = linp()

    l, h = 1, n
    ans = - 1
    while l <= h:
        m = (l + h) >> 1
        if chk(m):
            ans = m
            l = m + 1
        else:
            h = m - 1
    print(ans)


if __name__ == '__main__':
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    def linp(): return [int(i) for i in input().split()]

    logging.basicConfig(
        format="%(message)s",
        level=logging.WARNING,
    )
    logger = getLogger(__name__)
    logger.setLevel(logging.INFO)

    def debug(msg, *args):
        logger.info(f'{msg}={pprint.pformat(args)}')

    for _ in range(*linp()):
        solve()
