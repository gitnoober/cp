
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


def calcpr(n):
    d = collections.defaultdict(int)
    while n % 2 == 0:
        n //= 2
        d[2] += 1

    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            n //= i
            d[i] += 1
    if n > 1:
        d[n] += 1

    return d


def solve():

    N, = linp()
    a = linp()

    dic = collections.defaultdict(list)

    for i in a:
        x = calcpr(i)
        dic[i].append(x)

    debug("dic", dic)


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
