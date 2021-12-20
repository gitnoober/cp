
# DON'T SUBMIT UNLESS YOU'RE ABSOLUTELY SURE OR ATLEAST 70 % SURE !!!

import sys
import pprint
import logging
from logging import getLogger
import array
import collections
import io
import os
import heapq
import bisect
from math import ceil
# sys.setrecursionlimit(10 ** 9)

inf = float('inf')

def solve():

    for _ in range(*linp()):
        n, = linp()
        a = [(j, i) for i, j in enumerate(linp())]
        a.sort(key=lambda x: x[0], reverse=True)
        tot = 0
        i = 0
        res = [inf] * n
        diff = 1
        x0 = 1

        while i + 1 < n:
            x1 = (2 * diff * a[i][0]) + (2 * diff * a[i + 1][0])
            x2 = (2 * diff * a[i][0]) + 2 * (diff + 1) * a[i + 1][0]
            tot += min(x1, x2)
            if x1 < x2:
                res[a[i][1]] = diff + x0
                res[a[i + 1][1]] = x0 - diff
            else:
                res[a[i][1]] = diff + x0
                res[a[i + 1][1]] = x0 - diff
            diff += 1
            i += 2

        if n % 2:
            tot += 2 * diff * a[i][0]
            res[a[i][1]] = diff + x0

        print(tot)
        print(*[1] + res)


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
    solve()
