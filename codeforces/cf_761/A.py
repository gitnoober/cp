
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


import collections

for _ in range(int(input())):
    s = ''.join(sorted(input()))
    t = input()
    idx = 0
    for i in range(len(s)):
        if idx == 3:
            break
        if s[i] == t[idx]:
            idx += 1
    if idx < 3:
        print(s)
    else:
        d = collections.defaultdict(int)
        for i in s:
            d[i] += 1
        res = (d['a'] * 'a') + (d['c'] * 'c') + (d['b'] * 'b')
        for i in 'defghijklmnopqrstuvwxyz':
            res += d[i] * i
        print(res)
