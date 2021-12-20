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
    for i in range(*maps()):
        s = input()
        q = [list(maps()) for _ in range(*maps())]
        n = len(s)

        dp = [1]*n
        turn = 1
        st = []

        for i in range(n):
            if s[i] == ')':
                dp[i] = dp[st.pop()]
                turn = dp[i]
                continue
            
            if s[i] == '-':turn^=1
            if s[i] == '(':st.append(i)
            dp[i] = turn

        # debug("dp" , dp)
        pre = [[0 , 0] for _ in range(n)]

        for i in range(1 , n ):
            pre[i][0] += pre[i-1][0]
            pre[i][1] += pre[i-1][1]
            if s[i]  == '?':
                pre[i][dp[i]]+=1
        ans = []
        
        for l , r in q :
            if l == r :
                ans.append(1)
                continue
            ans.append(pre[r-1][dp[r-1]] - pre[l-1][dp[l-1]])

        print(*ans)

        
        

        





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
