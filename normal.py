
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


def check(dic, length):
    ct = 0
    for i in dic:
        if dic[i] % 2:
            ct += 1

    if (length % 2 and ct == 1) or ():
        return True


def solve():
    s = input()
    n = len(s)
    d = collections.Counter(s)
    if check(d, n):
        return 0

    ans = inf
    for i in range(n):
        if d[s[i]] % 2:
            N = 0
            for j in range(i, n):
                d[s[j]] -= 1
                N += 1
                if check(d, n - N):
                    ans = N
                    break
            break
    return ans


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
    print(solve())
