inf = float('inf')
import sys
import pprint
import logging
from logging import getLogger
import array
import collections
from math import gcd
# sys.setrecursionlimit(10 ** 9)


def solve():

	for _ in range(*maps()):
		n, = maps()
		b = [*maps()]
		a , gc = [b[0]] , b[0]
		for i in b[1:] :
			gc = gcd(gc, i)
			a.append(gc)

		if a == b :
			print(*a)
		else:
			print(-1)






if __name__ == '__main__':
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

    solve()
