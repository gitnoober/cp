inf = float('inf')
import sys
import pprint
import logging
from logging import getLogger
import array
import collections
import os
import io
from math import gcd

# sys.setrecursionlimit(10 ** 9)


def solve():

    for _ in range(*maps()):
        a, b, x = maps()

        if a < b :
            a , b = b , a
        
        ok = False
        while not ok and b > 0:
            if a == x or b == x or ((a-x)%b == 0 and a >= x):
                ok = True
                break

            if a < b :
                a , b = b , a

            a , b = b , a % b

        print('YES' if ok else 'NO')



if __name__ == '__main__':
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

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
