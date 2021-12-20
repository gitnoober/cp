
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

    def chk(l, idx):
        res = []
        for i in l:
            if i == l[idx]:
                continue
            res.append(i)
        return res == res[::-1]

    for _ in range(*linp()):
        n, = linp()
        a = linp()

        l, r = 0, n - 1
        while l < r and a[l] == a[r]:
            l += 1
            r -= 1

        if l == r or chk(a, l) or chk(a, r):
            print('YES')

        else:
            print('NO')


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
