inf = float("inf")
import sys
import pprint
import logging
from logging import getLogger

# sys.setrecursionlimit(10 ** 9)


def solve():

    for _ in range(*maps()):
        (n,) = maps()
        a = sorted(maps())
        b = sorted(maps())

        mx = -inf
        mi = inf

        for i in range(n):
            mx = max(mx, b[i] - a[i])
            mi = min(mi, b[i] - a[i])
        if mi >= 0 and mx <= 1:
            print("YES")
        else:
            print("NO")


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
