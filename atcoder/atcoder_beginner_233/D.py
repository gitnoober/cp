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


from collections import defaultdict


def solve():
    n, k = inp()
    a = list(inp())
    summ = 0
    prev = defaultdict(int)
    ans = 0

    for idx, i in enumerate(a):
        summ += i
        x = summ - k
        ans += prev[x]
        prev[summ] += 1

    print(ans + prev[k])


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
