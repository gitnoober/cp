
import sys
import pprint
import logging
from logging import getLogger

def input(): return sys.stdin.readline().rstrip("\r\n")


logging.basicConfig(format="%(message)s", level=logging.WARNING,)
logger = getLogger(__name__)
logger.setLevel(logging.INFO)


def debug(msg, *args):
    logger.info(f'{msg}={pprint.pformat(args)}')

# 30 MINUTES ATLEAST !!!!

###################################################################################################################


def msb(x):
    p = 0
    while 1 << p < x:
        p += 1

    if (1 << p) > x:
        p -= 1
    return p


arr = [0] * 20
maxn = int(2e5)
d = {}
d[0] = arr[:]
for i in range(1, maxn + 1):
    for j in range(20):
        if (1 << j) & i:
            continue
        arr[j] += 1
    d[i] = arr[:]


def solve():
    l, r = inp()
    L, R = l, r
    res = 0
    while l > 0 and r > 0:
        a, b = msb(l), msb(r)
        if a != b:
            break

        res += (1 << a)

        l -= (1 << a)
        r -= (1 << a)

    if res > 0:
        print(0)
        return

    a1 = d[L - 1][:]
    a2 = d[R][:]

    for j in range(20):
        a2[j] -= a1[j]

    mi = float('inf')
    for i in range(20):
        mi = min(mi, a2[i])

    print(mi)


if __name__ == '__main__':
    multi = True
    t = 1

    def inp(): return map(int, input().split())

    if multi:
        t = int(input())

    while t:
        t -= 1
        solve()
