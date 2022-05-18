
# DON'T SUBMIT UNLESS YOU'RE ABSOLUTELY SURE OR ATLEAST 70 % SURE !!!

import sys
import pprint
import logging
from logging import getLogger
import array
import collections
import io
import os
import heapq
import bisect

# sys.setrecursionlimit(10 ** 9)

inf = float('inf')
maxN = int(1e6) + 10
pr = [True] * maxN
pr[0] = pr[1] = False


for i in range(2, maxN):
    if pr[i]:
        for j in range(2 * i, maxN, i):
            pr[j] = False

tree = [0] * maxN


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
    while i <= maxN:
        tree[i] += x  # updating all the positions in the tree which are responsible for this index
        i += i & -i


pre = [0]
for i in range(1, maxN):
    pre.append(pre[-1] + pr[i])


def solve():

    n, = linp()
    a = [*linp()]

    ans = []

    for i in a:
        if i == 1:
            ans.append(1)
            continue

        sq = int(i**0.5)
        ans.append(pre[i] - pre[sq] + 1)
    print(*ans, sep='\n')


if __name__ == '__main__':
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    def linp(): return [int(i) for i in input().split()]

    logging.basicConfig(
        format="%(message)s",
        level=logging.WARNING,
    )
    logger = getLogger(__name__)
    logger.setLevel(logging.INFO)

    def debug(msg, *args):
        logger.info(f'{msg}={pprint.pformat(args)}')
    solve()
