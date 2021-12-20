
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

# let's do this by recursion


def printPattern(t, n):
    if t == n + 1:
        return

    for i in range(n - t):
        print(' ', end=' ')

    for i in range(t + 1):
        print(i, end=' ')

    for i in range(t - 1, 0, -1):
        print(i, end=' ')

    print(0)

    printPattern(t + 1, n)

    if t == n:
        return
    for i in range(n - t):
        print(' ', end=' ')

    for i in range(t + 1):
        print(i, end=' ')

    for i in range(t - 1, 0, -1):
        print(i, end=' ')

    print(0)


def single():
    return map(int, input().split())

# interior angle of a polygon is defined as angle b/w any two adjacent sides, i.e  180 * (n - 2) // n
# DON'T LOOK AT TEST CASES !!


# from itertools import permutations

def calc(x, y, n, val):
    return (x + val) >= (y / 100) * n


import collections


def C():
    for i in range(int(input())):
        n, k, x = single()
        s = input()
        precnt = 0
        suffcnt = 0
        for i in s:
            if i == '*':
                suffcnt += 1

        if suffcnt == 0:
            print(s)
            continue

        for i in s:
            if i == '*':
                precnt += 1
                suffcnt -= 1


# C()

from itertools import permutations


def f():
    s = '***'
    se = set()
    k = 2
    for i in permutations(s):
        st = ''
        for j in i:
            for jj in range(k + 1):
                st += 'b' * jj
            se.add(st)

    debug("se", se)


f()
