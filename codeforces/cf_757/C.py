# DON'T SUBMIT UNLESS YOU'RE ABSOLUTELY SURE OR ATLEAST 70 % SURE !!!

import pprint
import logging
from logging import getLogger
import io
import os

# sys.setrecursionlimit(10 ** 9)

inf = float("inf")
mod = int(1e9) + 7


def xorSum(arr, n):

    bits = 0

    for i in range(n):
        bits |= arr[i]

    ans = (bits * pow(2, n - 1, mod)) % mod

    return ans


def solve():

    for _ in range(*linp()):
        n, m = linp()
        mx = 0
        for i in range(m):
            l, r, val = linp()
            mx |= val
        print((mx * pow(2, n - 1, mod)) % mod)


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
