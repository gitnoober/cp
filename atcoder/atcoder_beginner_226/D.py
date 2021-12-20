inf = float('inf')
import sys
import pprint
import logging
from logging import getLogger
import array
import collections
import math
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


se = set()
n, = maps()
A = [[*maps()] for _ in range(n)]

for i in range(n):
    x1, y1 = A[i]
    for j in range(n):
        if i == j:
            continue
        x2, y2 = A[j]

        xx1 = x2 - x1
        yy1 = y2 - y1
        xx2 = x1 - x2
        yy2 = y1 - y2
        g1 = math.gcd(xx1, yy1)
        g2 = math.gcd(xx2, yy2)
        se.add((xx1 // g1, yy1 // g1))
        se.add((xx2 // g2, yy2 // g2))

print(len(se))
