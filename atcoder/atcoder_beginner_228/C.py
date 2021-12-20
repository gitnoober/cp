inf = float('inf')
import sys
import pprint
import logging
from logging import getLogger
import array
import collections

# sys.setrecursionlimit(10 ** 9)


def solve():
    n, k = maps()

    A = []
    B = []

    for i in range(n):
        a = list(maps())
        s = sum(a)
        A.append((i, s))
        B.append(s + 300)

    A.sort(key=lambda x: -x[1])

    mn = A[k - 1][1]

    for i in range(n):
        if B[i] >= mn:
            print('Yes')
        else:
            print('No')


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
