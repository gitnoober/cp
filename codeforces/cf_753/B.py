inf = float('inf')
import sys
import pprint
import logging
from logging import getLogger
import array
import collections

# sys.setrecursionlimit(10 ** 9)

def input(): return sys.stdin.readline().rstrip("\r\n")

def maps(): return [int(i) for i in input().split()]


logging.basicConfig(
    format="%(message)s",
    level=logging.WARNING,
)
logger = getLogger(__name__)
logger.setLevel(logging.INFO)


def debug(msg, *args):
    logger.info(f'{msg}={pprint.pformat(args)}')


for _ in range(*maps()):
    x0, n = maps()
    N = n % 4
    A = []
    tt = N
    for i in range(n, -1, -1):
        if N > 0:
            A.append(i)
            N -= 1
        else:
            break

    # print(A, tt)
    A.sort()
    ans = x0
    while A:
        x = A.pop(0)
        if x0 % 2:
            x0 += x
        else:
            x0 -= x
    print(x0)
