inf = float("inf")
import sys
import pprint
import logging
from logging import getLogger

# sys.setrecursionlimit(10 ** 9)


def solve():

    for _ in range(*maps()):
        s = input()
        d = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}

        se = set()
        x = y = 0
        for i in s:
            dx, dy = d[i]
            x, y = x + dx, y + dy
            se.add((x, y))

        for X, Y in se:
            x = y = 0
            for i in s:
                cx, cy = x, y
                dx, dy = d[i]
                cx, cy = cx + dx, cy + dy

                if cx == X and cy == Y:
                    continue
                x, y = cx, cy

            if x == y == 0:
                print(X, Y)
                break
        else:
            print(0, 0)


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
