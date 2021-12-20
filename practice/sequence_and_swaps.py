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
    
    for __ in range(*maps()):
        n , x = maps()
        a = list(maps())
        ans = 0
        for i in range(n):
            if sorted(a) == a :
                break
            if a[i] > x :
                a[i] , x = x , a[i]
                ans+=1
        print(ans if sorted(a) == a else - 1)




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
