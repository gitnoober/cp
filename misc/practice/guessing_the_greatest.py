inf = float("inf")
import sys
import pprint
import logging
from logging import getLogger

# sys.setrecursionlimit(10 ** 9)


def solve():

    def ask(l, r):
        if l == r:
            return -1

        print("?", l, r, flush=True)
        (x,) = maps()
        return x

    (n,) = maps()
    l, r = 1, n + 1

    while r - l > 1:
        m = (l + r) >> 1

        was = ask(l, r - 1)
        if was < m:
            if ask(l, m - 1) == was:
                r = m
            else:
                l = m
        else:
            if ask(m, r - 1) == was:
                l = m
            else:
                r = m

    print("!", l, flush=True)


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
