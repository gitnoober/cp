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
    a, b, c = inp()
    ans = []
    for i in range(1, 82):
        tobe = (b * pow(i, a)) + c
        if tobe < 0:
            continue

        if sum(map(int, str(tobe))) == i and tobe < 10**9:
            ans.append(tobe)

    print(len(ans), "\n", *ans)


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
