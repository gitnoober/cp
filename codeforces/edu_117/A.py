inf = float('inf')
import sys
import pprint
import logging
from logging import getLogger
import array
import collections
import os
# sys.setrecursionlimit(10 ** 9)

def main():
    osi = '/home/ps/Documents/cp/input.txt'
    oso = '/home/ps/Documents/cp/output.txt'
    if os.path.exists(osi):
        sys.stdin = open(osi , 'r')
        sys.stdout = open(oso , 'w')

def solve():

    def d(p1 , p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    for i in range(*maps()):
        x , y = maps()
        s = x + y
        if s % 2 == 0 :
            print(x//2 ,(y//2 + (y%2)))
        else:
            print(-1 , -1)
        

    





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
