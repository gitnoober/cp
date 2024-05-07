# DON'T SUBMIT UNLESS YOU'RE ABSOLUTELY SURE OR ATLEAST 70 % SURE !!!

import pprint
import logging
from logging import getLogger
import io
import os

# sys.setrecursionlimit(10 ** 9)

inf = float("inf")
n = int(3e5)


def solve():

    (N,) = linp()
    a = list(linp())
    tree = [0] * n

    def get_sum(i):
        s = 0
        while i > 0:
            s += tree[i]
            i -= i & -i
        return s

    def get_sum_segment(s, t):
        ans = get_sum(t) - get_sum(s - 1)
        return ans

    def add(i, x):  # index , value
        while i <= n:
            tree[
                i
            ] += x  # updating all the positions in the tree which are responsible for this index
            i += i & -i

    for i in a:
        x = get_sum(i - 1) + 1
        add(i, x)

    ans = get_sum(n - 1) + 1
    print(ans)


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
