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


def solve():
    (n,) = inp()
    a = list(inp())
    s = sum(a)

    if s % n == 0:
        print(0)
        return

    # avg = s // n + (1 if s % n else 0)
    # diff = s - (avg * (n - 1))
    # print(diff, avg, avg * (n - 1), s)
    print(1)


if __name__ == "__main__":
    multi = True
    t = 1

    def inp():
        return map(int, input().split())

    if multi:
        t = int(input())

    while t:
        t -= 1
        solve()
