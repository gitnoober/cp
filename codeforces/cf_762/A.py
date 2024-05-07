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
    s = input()
    if len(s) % 2:
        print("NO")
        continue
    n = len(s)
    if s[: n // 2] == s[n // 2 :]:
        print("YES")
    else:
        print("NO")
