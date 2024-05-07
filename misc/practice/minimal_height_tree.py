# DON'T SUBMIT UNLESS YOU'RE ABSOLUTELY SURE OR ATLEAST 70 % SURE !!!

import io
import logging
import os
import pprint

from logging import getLogger

# sys.setrecursionlimit(10 ** 9)

inf = float("inf")


def bi(arr, key):
    l, h = 0, len(arr) - 1
    ans = -1
    while l <= h:
        m = (l + h) >> 1
        if arr[m] < key:
            ans = l
            l = m + 1
        else:
            h = m - 1
    return ans


def solve():

    for _ in range(*linp()):
        (n,) = linp()
        a = list(linp())

        level = 0
        ans = 1
        c = 0

        for i in range(1, n):
            if a[i - 1] < a[i]:
                c += 1
            else:
                if level == 0:
                    ans += 1
                    level = c - 1
                else:
                    level -= 1
        print(ans)


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
