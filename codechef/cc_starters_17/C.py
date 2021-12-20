inf = float('inf')
import sys
import pprint
import logging
from logging import getLogger
import array
import collections
from bisect import bisect_left
# sys.setrecursionlimit(10 ** 9)

def cntinv(s):
    n = len(s)
    tree = [0]*(n+1)
    cnt = 0

    def get_sum(i):
        s = 0
        while i > 0:
            s += tree[i]
            i -= i & -i
        return s

    def get_sum_segment(s, t):
        ans = get_sum(t) - get_sum(s - 1)
        return ans


    def add(i, x):  # index , value
        while i <= n:
            tree[i] += x  # updating all the positions in the tree which are responsible for this index
            i += i & -i
    s = [int(i) for i in s]
    temp = sorted(s)
    for i in range(n):
        s[i] = bisect_left(temp, s[i]) + 1

    for i in range(n - 1 , -1, -1):
        cnt += get_sum(s[i] - 1)
        add(s[i], 1)
    return cnt


def solve():

    for _ in range(*maps()):
        n , m = maps() #all the strings are of same length
        ans , l , r , available , t = [-1]*n , 0 , n - 1 , [] , []
        for i in range(n):
            s = input()
            c0 = c1 = 0
            for j in range(m):
                c1 += (s[j] == '1')
                c0 += (s[j] == '0')

            if c0 == m :
                ans[l] = s
                l+=1
            elif c1 == m:
                ans[r] = s
                r-=1
            else:
                cs = cntinv(s)
                available.append((cs , c0 , c1 , s))

        available.sort(key= lambda x : (-x[1] , x[0]))
        j = 0
        for i in range(n):
            if ans[i] == -1 :
                ans[i] = available[j][3]
                j+=1

        for i in ans:
            t+=list(i)
        print(cntinv(t))




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
