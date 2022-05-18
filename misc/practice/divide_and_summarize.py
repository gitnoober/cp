inf = float('inf')
import sys
import pprint
import logging
from logging import getLogger
import array
import collections
import bisect
# sys.setrecursionlimit(10 ** 9)


def bi(a, key):
    l , h = 0 , len(a) - 1
    mid = - 1

    while l <= h :
        m = (l + h) >> 1

        if a[m] <= key:
            l = m + 1
            mid = m
        else:
            h = m - 1
    return mid + 1

def solve():

    n , tq = maps()
    a = sorted(maps())
    q = [[*maps()][0] for _ in range(tq)]

    poss = {sum(a)}

    def f(arr , midpt):

        if len(set(arr)) == 1 :
            x = sum(arr)
            poss.add(x)
            return x

        idx = bi(arr , midpt)
        s = sum(arr)
        s1 = sum(arr[:idx])
        s2 = s - s1

        poss.add(s1)
        poss.add(s2)

        A , B = arr[:idx] , arr[idx:]

        f(A , (A[0] + A[-1]) // 2)
        f(B , (B[0] + B[-1]) // 2)


    f(a , (a[0] + a[-1]) // 2)


    print('\n'.join(['Yes' if i in poss else 'No' for i in q]))





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
