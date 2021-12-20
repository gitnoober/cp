
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
from collections import deque


def goodDaysToRobBank(security, time):
    n = len(security)

    if time == 0:
        return [i for i in range(n)]

    if (2 * time) + 1 > n:
        return []

    lt, rt = [1], [1]
    curr = 1
    for i in range(1, n):
        if security[i - 1] >= security[i]:
            curr += 1
        else:
            curr = 1
        lt.append(curr)

    curr = 1
    for i in range(n - 2, -1, -1):
        if security[i] <= security[i + 1]:
            curr += 1
        else:
            curr = 1
        rt.append(curr)

    rt = rt[::-1]
    time += 1

    return [i for i in range(n) if lt[i] >= time and rt[i] >= time]


security = [5, 3, 3, 3, 5, 6, 2]
time = 2
x = goodDaysToRobBank(security, time)
print(x)

# Output: [0,1,2,3,4]
