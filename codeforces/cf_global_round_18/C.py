
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


def solve():
    n, = inp()
    a = input()
    b = input()

    xa = ya = 0
    xb = yb = 0  # 0 , 1

    ch = []
    incorrect = 0
    correct = 0

    for i in range(n):
        if a[i] != b[i]:
            incorrect += 1
        else:
            correct += 1

        ch.append((correct, incorrect))

        if a[i] == '0':
            xa += 1
        elif a[i] == '1':
            ya += 1

        if b[i] == '0':
            xb += 1
        elif b[i] == '1':
            yb += 1

    # debug("ch", ch, (xa, ya), (xb, yb))
    if a == b:
        print(0)
        return
    A = sorted([xa, ya])
    B = sorted([xb, yb])

    # if ya == 0 and yb != n:
    #     print(-1)
    #     return

    print(min(ch[-1]), (xa, ya), (xb, yb))


if __name__ == '__main__':
    multi = True
    t = 1

    def inp(): return map(int, input().split())

    if multi:
        t = int(input())

    while t:
        t -= 1
        solve()
