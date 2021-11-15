inf = float('inf')
import sys
import pprint
import logging
from logging import getLogger
import array
import collections

# sys.setrecursionlimit(10 ** 9)


def solve():

    for _ in range(*maps()):
        n, = maps()
        a = list(maps())
        cnt = [0] * 61
        for i in range(61):
            bit = (1 << i)
            for j in a:
                if bit & j:
                    cnt[i] += 1
        debug("cnt", cnt[:6][::-1])


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
