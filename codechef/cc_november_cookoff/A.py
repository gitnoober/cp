inf = float("inf")
import sys
import pprint
import logging
from logging import getLogger
import os

# sys.setrecursionlimit(10 ** 9)


def main():
    osi = "/home/ps/Documents/cp/input.txt"
    oso = "/home/ps/Documents/cp/output.txt"
    if os.path.exists(osi):
        sys.stdin = open(osi, "r")
        sys.stdout = open(oso, "w")


def solve():

    for _ in range(*maps()):
        (n,) = maps()
        A = []
        for i in range(1, 10**5, 2):
            if len(A) == n:
                break
            A.append(i)
        print(*A)


if __name__ == "__main__":
    main()

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
