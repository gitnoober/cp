inf = float("inf")
import sys
import pprint
import logging
from logging import getLogger

# sys.setrecursionlimit(10 ** 9)


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


for _ in range(*maps()):
    s = input()
    ab, ba = 0, 0
    for i in range(len(s) - 1):
        if s[i] + s[i + 1] == "ab":
            ab += 1
        elif s[i] + s[i + 1] == "ba":
            ba += 1

    if ab == ba:
        print(s)
        continue

    for i in range(len(s) - 1):
        print(s[i], end="")
    if ab > ba:
        print("a")
    else:
        print("b")
