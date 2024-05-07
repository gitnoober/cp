import sys
import pprint
import logging
from logging import getLogger


def input():
    return sys.stdin.readline().rstrip("\r\n")


logging.basicConfig(
    format="%(message)s",
    level=logging.WARNING,
)
logger = getLogger(__name__)
logger.setLevel(logging.INFO)


def debug(msg, *args):
    logger.info(f"{msg}={pprint.pformat(args)}")


# 30 MINUTES ATLEAST !!!!


###################################################################################################################
from math import ceil


def solve():
    x, y = inp()
    y -= x
    if y <= 0:
        print(0)
    else:
        print(ceil(y / 10))


if __name__ == "__main__":
    multi = False
    t = 1

    def inp():
        return map(int, input().split())

    if multi:
        t = int(input())

    while t:
        t -= 1
        solve()
