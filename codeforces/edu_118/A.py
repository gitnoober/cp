
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


for i in range(int(input())):
    x1, p1 = input().split()
    x2, p2 = input().split()

    p1, p2 = int(p1), int(p2)
    idx1, idx2 = len(x1) - 1, len(x2) - 1

    while idx1 >= 0 and x1[idx1] == '0':
        idx1 -= 1
        p1 += 1

    while idx2 >= 0 and x2[idx2] == '0':
        idx2 -= 1
        p2 += 1

    x1 = x1[:idx1 + 1]
    x2 = x2[:idx2 + 1]

    # print(idx1, idx2, p1, p2)
    if len(x1) + p1 > len(x2) + p2:
        print('>')
    elif len(x1) + p1 < len(x2) + p2:
        print('<')
    else:
        if x1 == x2 and p1 == p2:
            print('=')
        else:
            #x1 , x2 , p1 , p2
            if p1 == p2:
                if int(x1) > int(x2):
                    print('>')
                else:
                    print('<')
            else:
                x1 += '0' * p1
                x2 += '0' * p2
                if x1 > x2:
                    print('>')
                else:
                    print('<')
