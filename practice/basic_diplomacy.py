inf = float('inf')
import sys
import pprint
import logging
from logging import getLogger
import array
import collections

# sys.setrecursionlimit(10 ** 9)


def solve():
    n, m = map(int , input().split())
    f = [[int(i) for i in input().split()] for _ in range(m)]    
    ans , cnt = [-1] * m , [0]*(n+1)
    x, ok = (m+1)//2 , True

    for i , a in enumerate(f):
        if a[0] == 1 :
            ans[i] = a[1]
            cnt[a[1]]+=1
            if cnt[a[1]] > x :
                print('NO')
                return

    for i , a in enumerate(f):
        if ans[i] == -1:
            fl = 1
            for j in a[1:]:
                if cnt[j] < x :
                    cnt[j]+=1
                    ans[i] = j
                    fl = 0
                    break

            if fl == 1 :
                ok = False
                break

    print('YES' , '\n' , ' '.join(map(str , ans))) if ok else print('NO')




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

    for _ in range(*maps()):
        solve()
