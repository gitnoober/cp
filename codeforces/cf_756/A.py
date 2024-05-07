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
        (n,) = linp()
        if n % 2 == 0:
            print(0)
            continue
        ok = False
        for i in str(n):
            if int(i) % 2 == 0:
                ok = True
                break
        if ok:
            if int(str(n)[0]) % 2:
                print(2)
            else:
                print(1)
        else:
            print(-1)


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
