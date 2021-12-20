inf = float('inf')
import sys
import pprint
import logging
from logging import getLogger
import array
import collections
import math
# sys.setrecursionlimit(10 ** 9)

def input(): return sys.stdin.readline().rstrip("\r\n")

def maps(): return [int(i) for i in input().split()]


logging.basicConfig(
    format="%(message)s",
    level=logging.WARNING,
)
logger = getLogger(__name__)
logger.setLevel(logging.INFO)


def debug(msg, *args):
    logger.info(f'{msg}={pprint.pformat(args)}')

def lcm(a , b):
	return (a*b)//math.gcd(a, b)

for _ in range(*maps()):
	n, = maps()
	a = list(maps())
	l = 1
	ok = True
	for i in range(n):
		l = lcm(l, i+2)
		if l > int(1e9):
			break
		if a[i]%l == 0 :
			ok = False
			break
	print('YES' if ok else 'NO')

