# DON'T SUBMIT UNLESS YOU'RE ABSOLUTELY SURE OR ATLEAST 70 % SURE !!!

import pprint
import logging
from logging import getLogger
import collections
import io
import os

# sys.setrecursionlimit(10 ** 9)

inf = float("inf")
# mod = int(1e9) + 7
# mod = 998244353


def calc(length):
    if length % 2:
        return length // 2
    return (length // 2) - 1


def solve():

    for _ in range(*linp()):
        (n,) = linp()
        b = sorted(linp())

        left, right = [], []

        i = 0
        while i < n:
            left.append(b[i])
            i += 2

        i = 2 * n - 1
        while i > n:
            right.append(b[i])
            i -= 2

        a = left + right[::-1]
        pre = []

        for i in range(n):
            idx = calc(i + 1)
            pre.append(a[idx])

        tot = collections.deque()
        idx = n - 1

        for i in range(n):
            tot.appendleft(a[idx])
            pre.append(tot[calc(i + 1)])
            idx -= 1

        pre.sort()
        print(*a if pre == b and len(set(a)) == n else [-1])


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

    solve()
