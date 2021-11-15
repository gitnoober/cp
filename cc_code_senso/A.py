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
    n, = maps()
    a = [*maps()]
    ans1 = []
    # ans2 = []
    prev = 0
    for i in range(n - 1):
        x = a[i] & a[i + 1]
        if x > prev:
            ans1.append(x)
        else:
            ans1.append(prev)
        prev = x

    x = max(prev, a[-1] & a[-2])
    ans1.append(x)
    # debug("ans1", ans1, prev)
    print(*ans1)
