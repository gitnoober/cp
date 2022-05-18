inf = float('inf')
import sys
import pprint
import logging
from logging import getLogger
import array
import collections

# sys.setrecursionlimit(10 ** 9)

def input(): return sys.stdin.readline().rstrip("\r\n")

def maps(): return [int(i) for i in input().split()]


logging.basicConfig(
    format="%(message)s",
    level=logging.WARNING,
)
logger = getLogger(__name__)
logger.setLevel(logging.INFO)


def debug(msg, *args):
    logger.info(f'{msg}={pprint.pformat(args)}')


def platesBetweenCandles(s, queries):

    n = len(s)
    tree = [0] * (n + 1)

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
            # updating all the positions in the tree which are responsible for this index
            tree[i] += x
            i += i & -i

    def bi1(arr, val):
        l, h = 0, len(arr) - 1
        idx = - 1
        while l <= h:
            m = (l + h) >> 1
            if arr[m] >= val:
                idx = m
                h = m - 1
            else:
                l = m + 1
        return idx

    def bi2(arr, val):
        l, h = 0, len(arr) - 1
        idx = - 1
        while l <= h:
            m = (l + h) >> 1
            if arr[m] <= val:
                idx = m
                l = m + 1
            else:
                h = m - 1
        return idx

    indices = []

    for i in range(n):
        if s[i] == '*':
            add(i + 1, 1)
        else:
            indices.append(i)
    A = []
    for li, ri in queries:
        idx1 = bi1(indices, li)
        idx2 = bi2(indices, ri)

        if idx1 != -1 and idx2 != - 1:
            x, y = indices[idx1], indices[idx2]
            ans = get_sum_segment(x + 1, y + 1)
        else:
            ans = 0
        A.append(max(0, ans))
    return A


s = "***|**|*****|**||**|*"
queries = [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]
x = platesBetweenCandles(s, queries)
print(x)
