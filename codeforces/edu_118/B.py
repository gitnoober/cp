
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


from itertools import accumulate


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(1, (n // 2) + 1):
        print(a[i], a[0])


for i in range(int(input())):
    solve()
