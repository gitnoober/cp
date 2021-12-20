
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
maxn = int(1e5) + 10


def ceil(a, b):
    return (a + b - 1) // b


pr = [True] * maxn
pr[0] = pr[1] = False

for i in range(2, maxn):
    if pr[i]:
        for j in range(2 * i, maxn, i):
            pr[j] = False


def solve():
    n, k = linp()
    a, b = set(), [1]
    x = n // 2

    for i in range(2, n + 1):
        if i <= x:
            for j in range(i, n + 1, i):
                a.add(j)

        elif i > x and pr[i]:
            b.append(i)

    if k <= len(b):
        print('YES')
        for i in range(k):
            print(b[i], end=' ')
        print()

    elif k >= n - len(b):
        for i in range(k - (n - len(b))):
            a.add(b.pop())
        print('YES')
        print(*a)
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

    for __ in range(*linp()):
        solve()
