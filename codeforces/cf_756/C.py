# DON'T SUBMIT UNLESS YOU'RE ABSOLUTELY SURE OR ATLEAST 70 % SURE !!!

import pprint
import logging
from logging import getLogger
import collections
import io
import os

# sys.setrecursionlimit(10 ** 9)

inf = float("inf")


def check(a):
    n = len(a)
    d = collections.deque()
    a = collections.deque(a)

    _i, _j = 0, n - 1

    while len(a) > 1:
        if a[0] < a[-1]:
            d.appendleft(a.popleft())
        else:
            d.append(a.pop())
    aa = []
    if len(a):
        aa.append([a[0]] + list(d))
        aa.append(list(d) + [a[0]])
    else:
        aa.append(d)
    return aa


def solve():

    (n,) = linp()
    a = list(linp())

    if a[0] != n and a[-1] != n:
        print(-1)
        return

    x = check(a)

    def ans():

        for i in x:
            tx = check(i)
            for j in tx:
                if j == a:
                    return i

        return [-1]

    print(*ans())


if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    def linp():
        return [int(i) for i in input().split()]

    logging.basicConfig(
        format="%(message)s",
        level=logging.WARNING,
    )
    logger = getLogger(__name__)
    logger.setLevel(logging.INFO)

    def debug(msg, *args):
        logger.info(f"{msg}={pprint.pformat(args)}")

    for __ in range(*linp()):
        solve()
