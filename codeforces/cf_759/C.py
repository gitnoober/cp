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


for _ in range(int(input())):
    _len, k = map(int, input().split())
    a = list(map(int, input().split()))

    p, n = [], []
    for i in a:
        if i >= 0:
            p.append(i)
        else:
            n.append(i)
    p.sort(reverse=False)
    n.sort(reverse=True)
    sz1, sz2 = len(p), len(n)
    stop = []

    if sz1 > 0:
        curr = sz1 - 1
        stop.append(p[curr])
        curr -= k
        while curr >= 0:
            stop.append(p[curr])
            curr -= k

    if sz2 > 0:
        curr = sz2 - 1
        stop.append(-n[curr])
        curr -= k

        while curr >= 0:
            stop.append(-n[curr])
            curr -= k

    stop.sort()
    ans = (2 * sum(stop)) - stop[-1]
    print(ans)
