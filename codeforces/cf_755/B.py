inf = float('inf')
import sys
import pprint
import logging
from logging import getLogger
import array
import collections
from math import ceil
# sys.setrecursionlimit(10 ** 9)


def solve():
    for _ in range(*maps()):
        n, m = maps()
        print(ceil((n * m) / 3))


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
