
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
# mod = int(1e9) + 7
# mod = 998244353

# 30 MINUTES ATLEAST !!!!

import heapq


class MyHeap(object):
    def __init__(self, initial=None, key=lambda x, y: (-(y - x + 1), x)):
        self.key = key
        self.index = 0

        if initial:
            self._data = [(key(item), i, item) for i, item in enumerate(initial)]
            self.index = len(self._data)
            heapq.heapify(self._data)
        else:
            self._data = []

    def push(self, item):
        heapq.heappush(self._data, (self.key(item[0], item[1]), self.index, item))
        self.index += 1

    def pop(self):
        return heapq.heappop(self._data)[2]


def calc(l, r):
    if (r - l + 1) % 2:
        return (l + r) // 2
    else:
        return (l + r - 1) // 2


def solve():
    n = int(input())
    cnt = 0
    h = MyHeap()
    h.push((1, n))
    arr = [0] * (n + 1)

    while len(h._data):
        l, r = h.pop()
        mid = calc(l, r)
        if arr[mid] != 0:
            continue
        cnt += 1
        arr[mid] = cnt

        if l <= mid - 1:
            h.push((l, mid - 1))
        if mid + 1 <= r:
            h.push((mid + 1, r))

    print(*arr[1:])


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

    for _ in range(*linp()):
        solve()
