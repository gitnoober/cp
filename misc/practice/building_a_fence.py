inf = float('inf')
import sys
import pprint
import logging
from logging import getLogger
import array
import collections

# sys.setrecursionlimit(10 ** 9)


def solve():

    for __ in range(*maps()):
        n , k = maps()
        h = [*maps()]  # height of ground below
        mn , mx = h[0] , h[0] + k
        ok = True

        for i in range(1 , n - 1):
            d = h[i]
            u = h[i] + 2 * k - 1

            if mn >= u or mx <= d :
                ok = False

            mn = max(d , mn + 1 - k)
            mx = min(u , mx - 1 + k)

        d , u = h[n - 1] , h[n - 1] + k

        if mn < u and mx > d and ok:
            print('YES')
        else:
            print('NO')



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
