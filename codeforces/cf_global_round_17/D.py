# DON'T SUBMIT UNLESS YOU'RE ABSOLUTELY SURE OR ATLEAST 70 % SURE !!!

import pprint
import logging
from logging import getLogger
import io
import os

# sys.setrecursionlimit(10 ** 9)

inf = float("inf")
mod = 998244353


def solve():

    (n,) = linp()
    dp = [1, 1]
    for i in range(n - 2):
        dp.append(dp[-1] + dp[-2])
        dp = dp[1:]

    x = dp[-1]
    y = pow(pow(2, n, mod), mod - 2, mod)
    print((x * y) % mod)


if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    def linp():
        return [int(i) for i in input().split()]

    logging.basicConfig(
        format="%(message)s",
        level=logging.WARNING,
    )
    logger = getLogger(__name__)
    logger.setLevel(logging.INFO)

    def debug(msg, *args):
        logger.info(f"{msg}={pprint.pformat(args)}")

    solve()
