inf = float("inf")
import sys
import pprint
import logging
from logging import getLogger

# sys.setrecursionlimit(10 ** 9)


def solve():

    for _ in range(*maps()):
        a, b, p, q = maps()
        if a == p and b == q:
            print(0)
            continue

        if (a + b) % 2 == (p + q) % 2:
            print(2)
        else:
            print(1)


if __name__ == "__main__":

    def input():
        return sys.stdin.readline().rstrip("\r\n")

    def maps():
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
