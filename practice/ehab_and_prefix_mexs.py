
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


def check(a, b):
    maxn = 10**6
    check = [False] * maxn
    l = fl = 0
    n = len(a)
    for i in range(n):
        check[b[i]] = True
        while l < maxn and check[l]:
            l += 1

        if a[i] < l:
            return False

    return True


maxn = 1000005
ex = [0] * maxn

def solve():

    n, = linp()
    a = list(linp())
    b = [-1] * n

    for i in range(1, n):
        if a[i] != a[i - 1]:
            b[i] = a[i - 1]
            ex[a[i - 1]] = 1

    l = 0
    ex[a[-1]] = 1
    for i in range(n):
        while l < maxn and ex[l]:
            l += 1
        if b[i] == - 1:
            b[i] = l
            ex[l] = 1

    if check(a, b):
        print(*b)
    else:
        print(-1)


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
