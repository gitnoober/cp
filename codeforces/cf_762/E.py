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


def check(cnt, mex):
    free = 0
    for i in range(mex):
        if cnt[i] > 0:
            free += cnt[i] - 1
        else:
            if free > 0:
                free -= 1
            else:
                return False
    return True


def solve():
    (n,) = inp()
    sorted(inp())


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
