
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


from collections import defaultdict, deque

h, w, c, q = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(q)]

res = [0] * c
totlen = totlen2 = 0
ser, sec = set(), set()

for t, n, color in queries[::-1]:
    if t == 1 and n not in ser:
        res[color - 1] += w - totlen  # always be re-written, so don't worry
        ser.add(n)
        totlen2 += 1

    elif t == 2 and n not in sec:
        sec.add(n)
        totlen += 1
        res[color - 1] += h - totlen2

print(*res)
