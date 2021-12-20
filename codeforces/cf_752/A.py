inf = float('inf')
import sys
import pprint
import logging
from logging import getLogger
import array
import collections

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


for _ in range(*maps()):
	n, = maps()
	a = list(maps())
	curidx = 0
	ans = 0
	for i in range(n):
		curidx+=1
		if a[i] <= curidx:
			continue
		# debug("ai , curidx, before",a[i] , curidx)
		need = (a[i] - curidx)
		ans+=need
		curidx += need
		# debug("ai , curidx, after",a[i] , curidx)
	print(ans)

