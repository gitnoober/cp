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


for i in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))

    ok = [False] * (n + 1)
    idx = 1
    cnt = fl = 0
    for i in range(n):
        while idx <= n and ok[idx]:
            idx += 1

        if a[i] <= n and not ok[a[i]]:
            ok[a[i]] = True

        elif (a[i] // 2) - (1 if a[i] % 2 == 0 else 0) >= idx:
            cnt += 1
            ok[idx] = True
        else:
            fl = 1

    for i in range(1, n + 1):
        if not ok[i]:
            fl = 1
            break
    if fl:
        print("-1")
    else:
        print(cnt)
