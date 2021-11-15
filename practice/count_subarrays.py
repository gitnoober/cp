inf = float('inf')
import sys
import pprint
import logging
from logging import getLogger
import array
import collections

# sys.setrecursionlimit(10 ** 9)


def naive(arr):
    n = len(arr)
    cnt = 0
    for i in range(n):
        for j in range(i, n + 1):
            x = arr[i:j]
            if len(x) and sorted(x) == x:
                cnt += 1
    return cnt


def solve():
    for _ in range(*maps()):
        n, = maps()
        a = list(maps())
        dp = [1] * n
        for i in range(n - 1):
            if a[i + 1] >= a[i]:
                dp[i + 1] = dp[i] + 1

        ans = sum(dp)
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
