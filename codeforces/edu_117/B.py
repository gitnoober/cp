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
    
    for _ in range(*maps()):
        n , a , b = maps()
        left , right = [] , []
        for i in range(b+1 , n+1):
            left.append(i)
        
        for i in range(a , n+1):
            if len(left) < n//2:
                left.append(i)
        
        for i in range(1 , n + 1):
            if i not in left:
                right.append(i)

        final = left + right
        mi , mx = inf , 0
        for i in range(n):
            if i < n//2 :
                mi = min(mi , final[i])
            else:
                mx = max(mx , final[i])

        if mi == a and mx == b :
            print(*final) 
        else:
            print(-1)




    





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
