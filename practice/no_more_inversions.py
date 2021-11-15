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
    n , k = maps()
    x = 2*k - n
    p = list(range(1 , x))
    p += list(range(k , x-1, -1))
    print(*p)
    #the number of inversions doesn't increase while swapping values from x to k in the permutation , it remains the same
    #if we swap values from 1 to x-1 with x to k , then the inversions will increase.
    
