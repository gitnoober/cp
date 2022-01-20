
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
    n, k, x = inp()
    s = input()
    cnt0 = 0
    for i in s:
        if i == '*':
            cnt0 += 1

    if x == 1:
        print('b' if cnt0 == n else 'a' * (n - cnt0))

        return

    till = 1
    i = n - 1
    while i > -1:
        cnt = 0
        if s[i] == '*':
            while i > - 1 and s[i] == '*':
                cnt += 1
                i -= 1

        if cnt >= till:


if __name__ == '__main__':
    multi = True
    t = 1

    def inp(): return map(int, input().split())

    if multi:
        t = int(input())

    while t:
        t -= 1
        solve()
