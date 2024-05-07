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


def OK(k, A, h):
    a = A[:]
    acc = 0
    ans = len(A) * k
    n = len(A)
    for i in range(n):
        x = a[i] + (k - 1)
        if i + 1 < n and x >= a[i + 1]:
            acc += (x - a[i + 1]) + 1

        if ((i + 1) * k) - acc >= h:
            return True

    ans -= acc
    return True if ans >= h else False


for i in range(int(input())):
    n, h = map(int, input().split())
    a = list(map(int, input().split()))
    lo, hi = 0, 10**18
    ans = -1
    while lo <= hi:
        m = (lo + hi) >> 1
        if OK(m, a, h):
            hi = m - 1
            ans = m
        else:
            lo = m + 1

    print(ans)
