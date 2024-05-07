inf = float("inf")
import sys
import pprint
import logging
from logging import getLogger

# sys.setrecursionlimit(10 ** 9)


def solve():

    s, t, x = maps()
    ok = False
    if s <= t:
        while s <= t:
            if s > x:
                ok = True
                break
            s += 1
            s %= 24

    else:
        a = []
        for i in range(s, 24):
            a.append(i)
        for i in range(t + 1):
            a.append(i)
        x += 1
        x %= 24
        if x in a:
            ok = True

    if ok:
        print("Yes")
    else:
        print("No")


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
