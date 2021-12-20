
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


from bisect import bisect_left  # e < x

n, q = map(int, input().split())
a = sorted(map(int, input().split()))
ans = []
for i in range(q):
    x = int(input())
    ans.append(n - bisect_left(a, x))  # atleast x
print(*ans)
