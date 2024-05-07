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
    n = int(input())
    s = input()
    curr = i = 1
    x = s[0]
    ans = 0
    while i < n:

        while i < n and x == s[i]:
            curr += 1
            i += 1
        ans += curr * (curr - 1) // 2
        curr = 0
        x = s[i] if i < n else None

    return ans


if __name__ == "__main__":
    print(solve())
