
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

    a, b = map(str, input().split())

    if len(a) > len(b):
        b = '0' * (len(a) - len(b)) + b

    if len(b) > len(a):
        a = '0' * (len(b) - len(a)) + a
    ans = 'Easy'
    for j in range(len(a) - 1, -1, -1):
        x, y = int(a[j]), int(b[j])
        if x + y > 9:
            ans = 'Hard'
            break
    print(ans)


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
