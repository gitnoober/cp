# DON'T SUBMIT UNLESS YOU'RE ABSOLUTELY SURE OR ATLEAST 70 % SURE !!!

import pprint
import logging
from logging import getLogger
import io
import os

# sys.setrecursionlimit(10 ** 9)

inf = float("inf")
# mod = int(1e9) + 7
# mod = 998244353


def solve():

    for _ in range(*linp()):
        (n,) = linp()
        a = sorted(linp(), reverse=True)
        idx = n - 1
        if a[-1] == 0:
            while idx >= 0 and a[idx] == 0:
                idx -= 1
            print(idx + 1)
            continue

        ans = a[-1] * n
        for i in range(n - 1):
            a[i] -= a[-1]
        a[-1] = 0
        while idx >= 0 and a[idx] == 0:
            idx -= 1

        print(ans + idx + 1)


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
