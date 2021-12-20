
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


def f(s, d):
    cnt = 0
    n = len(s)
    for i in d:
        j = 0

        lst = n - 1
        c1 = c2 = fst = 0

        while lst >= 0 and s[lst] == i:
            lst -= 1
            c1 += 1

        while fst < n and s[fst] == i:
            fst += 1
            c2 += 1

        cnt = max(cnt, c1, c2)

    return cnt


def solve():

    n, k = linp()
    s = input().strip()

    d = collections.defaultdict(int)
    for i in s:
        d[i] += 1

    if k == 0:
        return n if len(d) == 1 else -1

    if k == 1:
        return f(s, d)

    # for i in d :
        # divide it into blocks


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
        x = solve()
        print(x)
