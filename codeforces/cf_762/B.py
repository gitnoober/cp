import sys
import pprint
import logging
from logging import getLogger


def input():
    return sys.stdin.readline().rstrip("\r\n")


logging.basicConfig(
    format="%(message)s",
    level=logging.WARNING,
)
logger = getLogger(__name__)
logger.setLevel(logging.INFO)


def debug(msg, *args):
    logger.info(f"{msg}={pprint.pformat(args)}")


# 30 MINUTES ATLEAST !!!!

###################################################################################################################


for _ in range(int(input())):
    n = int(input())
    i = 1
    se = set()
    while i * i <= n:
        if i * i * i <= n:
            se.add(i * i * i)
        se.add(i * i)
        i += 1
    print(len(se))
