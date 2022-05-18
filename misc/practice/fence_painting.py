inf = float('inf')
import sys
import pprint
import logging
from logging import getLogger
import array
import collections

# sys.setrecursionlimit(10 ** 9)


def solve():

    n , m = maps()
    a = [*maps()]
    b = [*maps()]
    c = [*maps()]
    C = c[:]

    diff = [[] for _ in range(n + 1)]
    for i in range(n):
        if a[i] != b[i]:
            diff[b[i]].append(i)

    last = -1
    if len(diff[c[m - 1]]) > 0 :
        last = diff[c[m - 1]].pop()
    else:
        for i in range(n):
            if a[i] == b[i] == c[m - 1]:
                last = i
                break

    if last == -1:
        print('NO')
        return

    c[m - 1] = last
    for i in range(m - 1):
        if diff[c[i]]:
            c[i] = diff[c[i]].pop()
        else:
            c[i] = last

    for i in range(m):
        a[c[i]] = C[i]

    if a != b :
        print('NO')
        return

    print('YES')
    print(*map(lambda x : x + 1 , c))







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
