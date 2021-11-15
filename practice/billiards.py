inf = float('inf')
import sys
import pprint
import logging
from logging import getLogger
import array
import collections

# sys.setrecursionlimit(10 ** 9)


def solve():
    mod = 1000000009
    maxn = 10**6 + 5
    dp = array.array('i', [0 for i in range(maxn + 1)])
    dp[0] = 1
    for i in range(maxn):
        dp[i] += dp[i - 2] + dp[i - 3]
        dp[i] %= mod

    for _ in range(*maps()):
        n, = maps()
        print(dp[n])


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
