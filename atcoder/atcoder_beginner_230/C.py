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
# mod = int(1e9) + 7
# mod = 998244353


def solve():

    n, a, b = linp()
    p, q, r, s = linp()

    k = (p - a) - 1
    numrows = q - p + 1
    numcols = s - r + 1
    arr = [['.' for _ in range(numcols)] for __ in range(numrows)]

    sl, sr = max(1 - a, 1 - b), min(n - a, n - b)
    ml, mr = max(1 - a, b - n), min(n - a, b - 1)

    for k in range(p - a - 1, q - a + 1):

        if a + k > q:
            break

        if sl <= k <= sr and a + k >= p and b + k >= r and b + k <= s:
            rw, cl = (a + k) - p, (b + k) - r
            arr[rw][cl] = '#'

        if ml <= k <= mr and a + k >= p and b - k >= r and b - k <= s:
            rw, cl = (a + k) - p, (b - k) - r
            arr[rw][cl] = '#'

    for i in arr:
        print(''.join(i))


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
