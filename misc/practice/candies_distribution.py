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


(n,) = maps()
l = list(maps())
r = list(maps())
a = [n - l[i] - r[i] for i in range(n)]
flag = 0
for i in range(n):
    kl = kr = 0
    for j in range(n):
        if a[j] > a[i]:
            if j < i:
                kl += 1
            else:
                kr += 1
    if kl != l[i] or kr != r[i]:
        flag = 1
        break

if not flag:
    print("YES")
    print(*a)
else:
    print("NO")
