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
    (n,) = maps()
    a = list(maps())

    if n % 2 == 0:
        print("YES")
        continue

    ok = False
    for i in range(1, n):
        if a[i] <= a[i - 1]:
            ok = True
    print(["NO", "YES"][ok])


"""
a[i] <= a[i-1]
5 , 3 -- > 3 <= 5
a[i+1] <= a[i]
this proves what ?
5 3 2



"""
