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
        a = list(linp())
        cnt = 0
        for i in range(n):
            while a[i] % 2 == 0:
                a[i] //= 2
                cnt += 1
        a.sort()
        print((a[-1] * (1 << cnt)) + sum(a[: n - 1]))
        # print(sum(a), (1 << cnt))


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
