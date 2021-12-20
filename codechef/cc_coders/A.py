
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

    for _ in range(*linp()):
        n, k = linp()
        h = [int(i) for i in str(n)]
        for i in range(len(h)):
            if h[i] == 0 and k > 0:
                h[i] += 1
                k -= 1

        heapq.heapify(h)
        while k > 0:
            x = heapq.heappop(h)
            if x == 9:
                heapq.heappush(h, x)
                break
            k -= 1
            heapq.heappush(h, x + 1)

        pr = 1
        for i in h:
            pr *= i

        print(pr)


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
