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

# def perms(arr):
# 	se = []


def slv():
    arr = list(map(int, input().split()))
    mx = arr[-1]
    bc = mx - arr[0]
    a = mx - bc  # this is a
    for i in range(7):
        for j in range(7):
            if i == j:
                continue
            if arr[i] + arr[j] == bc:
                b, c = arr[i], arr[j]

    print(a, b, c)


for _ in range(int(input())):
    slv()
