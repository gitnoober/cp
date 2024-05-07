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


def ceil(a, b):
    return (a + b - 1) // b


def debug(msg, *args):
    logger.info(f"{msg}={pprint.pformat(args)}")


(tc,) = maps()
while tc:
    tc -= 1

    n, k = maps()
    if k == 1:
        print(n - 1)
        continue

    time = 0
    cnt = 0
    f = 0
    cur = 0
    while f < n - 1:
        if cnt == 0:
            f += 1
            cur = 2
        else:
            if cur > k:
                time += ceil((n - 1 - f), k)
                break
            f += min(cur, k)
            cur += cur
        time += 1
        cnt += 1
    print(time)
