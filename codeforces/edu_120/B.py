
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
    n, = inp()
    a = list(inp())
    s = input()

    d = {}
    cnt0 = cnt1 = 0

    for idx, i in enumerate(a):
        d[i] = idx
        if s[idx] == '1':
            cnt1 += 1
        else:
            cnt0 += 1

    res = [None] * n
    end = n
    for i in range(n, 0, -1):
        if cnt1 > 0:
            idx = d[i]
            if s[idx] == '1':
                res[idx] = end
                cnt1 -= 1
                end -= 1
        else:
            break

    st = 1
    for i in range(1, n + 1):
        if cnt0 > 0:
            idx = d[i]
            if s[idx] == '0':
                res[idx] = st
                st += 1
                cnt0 -= 1
        else:
            break
    print(*res)


if __name__ == '__main__':
    multi = True
    t = 1

    def inp(): return map(int, input().split())

    if multi:
        t = int(input())

    while t:
        t -= 1
        solve()
