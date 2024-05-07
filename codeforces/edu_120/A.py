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


from collections import Counter


def solve():
    ar = sorted(inp())
    if ar[-1] == sum(ar[:2]):
        print("YES")
        return

    c = Counter(ar)
    if len(c) > 2:
        print("NO")
        return

    x = None
    for i in c:
        if c[i] == 1:
            x = i

    print("YES" if x > 1 and x % 2 == 0 else "NO")


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
