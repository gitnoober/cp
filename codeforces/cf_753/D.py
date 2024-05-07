inf = float("inf")
import sys
import pprint
import logging
from logging import getLogger

# sys.setrecursionlimit(10 ** 9)


def input():
    return sys.stdin.readline().rstrip("\r\n")


def maps():
    return [int(i) for i in input().split()]


logging.basicConfig(
    format="%(message)s",
    level=logging.WARNING,
)
logger = getLogger(__name__)
logger.setLevel(logging.INFO)


def debug(msg, *args):
    logger.info(f"{msg}={pprint.pformat(args)}")


for _ in range(*maps()):
    (n,) = maps()
    a = list(maps())
    s = input()
    R = []
    B = []
    for i in range(n):
        if s[i] == "R":
            R.append(a[i])
        else:
            B.append(a[i])

    B.sort()
    R.sort()

    ans = []
    ct = 1
    for i in range(len(B)):
        if B[i] < ct:
            break
        ans.append(ct)
        ct += 1
    for i in range(len(R)):
        if R[i] > ct:
            break
        ans.append(ct)
        ct += 1
    if list(range(1, n + 1)) == ans:
        print("YES")
    else:
        print("NO")

# It is possible to sort all the Blue color numbers to take the place of 1 to k numbers and the red number to take the place of k+1 , n
