
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


h, w = map(int, input().split())
arr = []
for i in range(h):
    arr.append(list(input()))

# for i in arr:
#     debug("i", ''.join(i))
p = [(0, -1), (0, 1), (1, 0), (-1, 0)]

for i in range(h):
    for j in range(w):
        if arr[i][j] == '.':
            se = set()
            for k in range(4):
                dx, dy = p[k]
                if i + dx < h and j + dy < w:
                    se.add(arr[i + dx][j + dy])

            for k in range(1, 6):
                if str(k) not in se:
                    arr[i][j] = str(k)
                    break
for i in arr:
    print(''.join(i))
