import sys
import pprint
import logging
from logging import getLogger


def input():
    return sys.stdin.readline().rstrip("\r\n")


logging.basicConfig(
    format="%(message)s",
    level=logging.WARNING,
)
logger = getLogger(__name__)
logger.setLevel(logging.INFO)


def debug(msg, *args):
    logger.info(f"{msg}={pprint.pformat(args)}")


# 30 MINUTES ATLEAST !!!!


###################################################################################################################
from math import gcd


def sieve():
    N = 2 * 10**5
    prime = [True] * N
    prime[0] = prime[1] = False
    for i in range(2, N):
        if prime[i]:
            for j in range(i + i, N, i):
                prime[j] = False
    lis = []
    for i in range(2, N):
        if prime[i]:
            lis.append(i)
    return lis


l = sieve()


for i in range(int(input())):
    n = int(input())
    for j in l:
        gc = gcd(j, n - j - 1)
        if gc == j or gc == n - j - 1:
            continue
        if gc == 1:
            print(j, n - j - 1, 1)
            break
