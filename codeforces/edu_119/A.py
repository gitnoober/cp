
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


def cidx(i, n):
    return (i + 1) % n


for i in range(int(input())):
    s = input()
    n = len(s)

    cnt0 = cnt1 = 0
    for i in s:
        if i == 'N':
            cnt1 += 1
    if cnt1 == 1:
        print('NO')
    else:
        print('YES')
