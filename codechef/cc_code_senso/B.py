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


def sahid():
    print("SAHID")


def ramadhir():
    print("RAMADHIR")


for _ in range(*maps()):
    (n,) = maps()
    s = input() + "-1"
    prev = s[0]
    cnt = 0
    for i in range(1, n + 1):
        if s[i] != prev:
            cnt += 1
            prev = s[i]
    if cnt == 1:
        sahid()
    elif cnt == 2:
        ramadhir()
    else:
        if cnt % 3 <= 1:
            sahid()
        else:
            ramadhir()
