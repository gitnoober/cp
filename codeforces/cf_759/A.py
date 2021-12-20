
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


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    tall = 1
    i = 0
    while i < n:
        if i + 1 < n and a[i] == a[i + 1] == 0:
            tall = - 1
            break
        if i - 1 >= 0 and a[i - 1] == a[i] == 1:
            tall += 5
            # i += 1
        elif a[i] == 1:
            tall += 1
        i+=1
    print(tall)
