# DON'T SUBMIT UNLESS YOU'RE ABSOLUTELY SURE OR ATLEAST 70 % SURE !!!

import pprint
import logging
from logging import getLogger

# sys.setrecursionlimit(10 ** 9)

inf = float("inf")
# mod = int(1e9) + 7
# mod = 998244353


def solve():

    s = input().strip()
    t = "oxx" * 100

    if s in t:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    # input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

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
