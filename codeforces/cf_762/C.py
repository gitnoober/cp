
import sys
import pprint
import logging
from logging import getLogger

def input(): return sys.stdin.readline().rstrip("\r\n")


logging.basicConfig(format="%(message)s", level=logging.WARNING,)
logger = getLogger(__name__)
logger.setLevel(logging.INFO)


def debug(msg, *args):
    logger.info(f'{msg}={pprint.pformat(args)}')

# 30 MINUTES ATLEAST !!!!

###################################################################################################################


def solve():
    a, s = inp()
    b = 0
    mul = 1
    fl = 0
    while s:
        p = s % 10
        q = a % 10
        s //= 10
        a //= 10
        if p < q:
            if not ((s % 10) == 1):
                fl = 1
                break
            p += 10
            s //= 10

        b += mul * (p - q)
        mul *= 10

    if a:
        fl = 1

    print(-1 if fl else b)


if __name__ == '__main__':
    multi = True
    t = 1

    def inp(): return map(int, input().split())

    if multi:
        t = int(input())

    while t:
        t -= 1
        solve()
