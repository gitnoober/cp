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


n, q = maps()
front, back = [-1] * (n + 1), [-1] * (n + 1)

while q:
    q -= 1
    a = list(maps())
    if a[0] == 1:
        x, y = a[1], a[2]
        front[y] = x
        back[x] = y

    elif a[0] == 2:
        x, y = a[1], a[2]
        front[y] = -1
        back[x] = -1

    else:
        x = a[1]
        while front[x] != -1:
            x = front[x]

        ans = []
        while x != -1:
            ans.append(x)
            x = back[x]
        print(len(ans), *ans)
