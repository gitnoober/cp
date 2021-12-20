
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

    a = []
    for i in range(2):
        s = input()
        for j in range(len(s)):
            if s[j] == '#':
                a.append((i, j))

    if len(a) <= 1:
        print('YES')
        return

    check = [False] * len(a)

    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                continue

            if abs(a[i][0] - a[j][0]) == 1 and (a[i][1] - a[j][1]) == 0:
                check[i] = check[j] = True

            if abs(a[i][1] - a[j][1]) == 1 and (a[i][0] - a[j][0]) == 0:
                check[i] = check[j] = True
    if all(check):
        print('Yes')
    else:
        print('No')


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
    solve()
