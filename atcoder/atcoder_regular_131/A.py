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


a = input().strip()
b = input().strip()

if int(b) % 2 == 0:
    x = str(int(b) // 2) + "0" + a
else:
    x = str(int(b) // 2) + "5" + a

print(int(x))
