
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


n = int(input())
d = {}
mx = 0
ans = -1
for i in range(n):
    s = input()
    d[s] = d.get(s, 0) + 1
    if d[s] > mx:
        mx = d[s]
        ans = s
print(ans)
