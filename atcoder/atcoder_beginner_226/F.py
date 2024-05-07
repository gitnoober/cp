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


from itertools import permutations

mod = 998244353


def naive(n):
    ans = 0
    a = list(range(1, n + 1))
    for i in permutations(a):
        t = 0
        for j in range(n):
            if i[j] != a[j]:
                t += 1
        ans += max(1, t)

    return ans


for i in range(1, 9):
    print(naive(i), i)
