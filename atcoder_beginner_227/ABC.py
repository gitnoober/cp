inf = float('inf')
import sys
import pprint
import logging
from logging import getLogger
import array
import collections
from math import ceil, sqrt
import bisect

# sys.setrecursionlimit(10 ** 9)


def naive(n):
    ans = 0
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            # if i * j > n:
            #     break
            for k in range(j, n + 1):
                # if i * j * k > n:
                #     break
                if i * j * k <= n:
                    ans += 1
    return ans


def solve():

    n, = maps()

    ans = 0
    for a in range(1, n + 1):
        if n < a**3:
            break
        for b in range(a, n + 1):
            if n < a * b * b:
                break
            ans += (n // (a * b)) - b + 1

    print(ans)


if __name__ == '__main__':
    def input(): return sys.stdin.readline().rstrip("\r\n")

    def maps(): return [int(i) for i in input().split()]

    logging.basicConfig(
        format="%(message)s",
        level=logging.WARNING,
    )
    logger = getLogger(__name__)
    logger.setLevel(logging.INFO)

    def debug(msg, *args):
        logger.info(f'{msg}={pprint.pformat(args)}')

    solve()
