inf = float('inf')
import sys
import pprint
import logging
from logging import getLogger
import array
import collections
import os
import math
# sys.setrecursionlimit(10 ** 9)

def main():
    osi = '/home/ps/Documents/cp/input.txt'
    oso = '/home/ps/Documents/cp/output.txt'
    if os.path.exists(osi):
        sys.stdin = open(osi , 'r')
        sys.stdout = open(oso , 'w')

def solve():
    n, m = maps()
    a = [*maps()]
    b = [*maps()]

    gc = 0 
    """
    gcd(a , b) - is a divisor of |a - b| , also gcd(a, b) = gcd(a - b , b)
    so gcd(a1 + bj , a2 + bj , ...) is divisor of a1 - a2 -- > gcd(a1 + bj , a1 - a2 , a1 - a3 ,a1 - aN) -- >  gcd(a1 + bj , gc)
    
    """
    for i in range(1, n):
        gc = math.gcd(gc, a[i] - a[0])
    
    print(*[math.gcd(a[0] + v , gc) for v in b])
    



if __name__ == '__main__':
    main()
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
