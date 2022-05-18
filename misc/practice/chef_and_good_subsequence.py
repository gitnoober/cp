inf = float('inf')
import sys
import pprint
import logging
from logging import getLogger
import array
import collections
mod = 1000000007
# sys.setrecursionlimit(10 ** 9)


def solve():

    n, k = maps()
    a = [*maps()]

    dic = collections.defaultdict(int)

    for i in a:
        dic[i] += 1

    freq = []

    for i in dic:
        freq.append(dic[i])

    m = len(freq)  # max possible

    k = min(k, m)
    dp = [[0 for _ in range(m + 1)] for __ in range(k + 1)]

    for i in range(m + 1):
        dp[0][i] = 1

    for i in range(1, k + 1):
        for j in range(i, m + 1):
            dp[i][j] = dp[i][j - 1] + (dp[i - 1][j - 1] * freq[j - 1])
            dp[i][j] %= mod

    res = 0
    for i in range(k + 1):
        res += dp[i][m]
        res %= mod
    print(res)


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
