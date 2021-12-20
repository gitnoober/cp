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

    for _ in range(*maps()):
        n, = maps()
        a = list(maps())
        s = sum(a)
        if s % 3 :
            print(-1)
            continue

        inc , dec = 0 , 0
        for i in a:
            if i % 3 == 0 :
                continue
            x = i % 3
            if x == 1 :
                dec+=1
            else:
                inc+=1
        x = min(inc , dec)
        dec-=x
        inc-=x
        while inc > 0 :
            x+= 2
            inc-=3
        while dec > 0 :
            x+=2
            dec-=3
        print(x)

        
        




    





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
