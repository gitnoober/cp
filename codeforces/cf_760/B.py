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


for i in range(int(input())):
    n = int(input())
    a = list(input().split())
    word = []
    for i in range(len(a)):
        if i == 0:
            word.append(a[i][0])
            word.append(a[i][1])
            prev = a[i][1]
        else:
            if a[i][0] != prev:
                if a[i][0] == "a":
                    word.append("a")
                if i + 1 < len(a):
                    word.append(a[i + 1][0])
                    prev = a[i + 1][0]
            else:
                word.append(a[i][1])

    print("".join(word))
