# DON'T SUBMIT UNLESS YOU'RE ABSOLUTELY SURE OR ATLEAST 70 % SURE !!!

import pprint
import logging
from logging import getLogger
import io
import os

# sys.setrecursionlimit(10 ** 9)

inf = float("inf")


def solve():

    for _ in range(*linp()):
        n, l, r, k = linp()
        A = list(linp())
        a = []
        for i in A:
            if i < l or i > r:
                continue
            a.append(i)
        a.sort()
        cnt = 0
        for i in a:
            if k - i >= 0:
                k -= i
                cnt += 1

        print(cnt)


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
