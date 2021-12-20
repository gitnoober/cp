
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


def sol1(n, p, q, s):
    ok = False
    for fl in range(2):
        a = [0, 0]
        for i in s:
            if i == '0':
                fl ^= 1
            a[fl] += 1

        totx, toty = a
        if totx >= p and toty >= q and (totx - p) % 2 == 0 and (toty - q) % 2 == 0:
            ok = True

    # return 'YES' if ok else 'NO'
    return ok


def solve():

    n, p, q = map(lambda x: abs(int(x)), input().split())
    s = input()
    ok = False
    for curr in range(2):
        x = y = 0
        for i in s:
            if i == '1':
                if curr == 0:
                    x += 1
                else:
                    y += 1
            else:
                curr ^= 1
                if curr == 0:
                    x += 1
                else:
                    y += 1

        if x >= p and y >= q and (x - p) % 2 == 0 and (y - q) % 2 == 0:
            ok = True

    # print('YES' if ok else 'NO')
    an2 = sol1(n, p, q, s)
    if an2 != ok:
        debug("an2 , ok ", an2, ok)


if __name__ == '__main__':
    # input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

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
