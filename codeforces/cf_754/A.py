inf = float("inf")
import sys
import pprint
import logging
from logging import getLogger

# sys.setrecursionlimit(10 ** 9)


def solve():
    for _ in range(*maps()):
        a1, a2, a3 = maps()
        if a1 + a3 == 2 * a2:
            print(0)
            continue

        s = ((a1 + a3) - (2 * a2)) % 3
        ans = s
        print(min(ans, 1))


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
