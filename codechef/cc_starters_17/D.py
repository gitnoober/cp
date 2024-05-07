inf = float("inf")
import sys
import pprint
import logging
from logging import getLogger

# sys.setrecursionlimit(10 ** 9)


def solve():

    def Bob():
        print("Bob")

    def Alice():
        print("Alice")

    for _ in range(*maps()):
        (n,) = maps()
        s = input()

        c0 = c1 = 0
        for i in s:
            if i == "0":
                c0 += 1
            else:
                c1 += 1

        x = min(c0, c1)
        if x == 0:
            Bob()
        elif x == 1:
            Alice()
        else:
            Bob() if n % 2 == 0 else Alice()


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
