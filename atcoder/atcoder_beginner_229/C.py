
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

# sys.setrecursionlimit(10 ** 9)

inf = float('inf')

def solve():

    n, w = linp()
    A = [linp() for _ in range(n)]
    A.sort(key=lambda x: (-x[0], -x[1]))
    # debug("A", A)
    ans = 0
    for a, b in A:
        x = min(b, w)
        ans += x * a
        w -= x

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
    solve()
