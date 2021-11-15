inf = float('inf')
import sys
import pprint
import logging
from logging import getLogger
import array
import collections

# sys.setrecursionlimit(10 ** 9)


class DisjointSetUnion:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.size = [1] * n
        self.numsets = n

    def find(self, x):
        xcopy = x
        while self.parent[x] != x:
            x = self.parent[x]
        while xcopy != x:
            xcopy, self.parent[xcopy] = self.parent[xcopy], x
        return x

    def union(self, x, y):
        a, b = self.find(x), self.find(y)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.size[a] += self.size[b]  # sz.a > sz.b
            self.parent[b] = a
            self.numsets -= 1

    def get_size(self, x):
        return self.size[self.find(x)]

    def __len__(self, x):  # number of components
        return self.numsets


def solve():

    n, k, p = maps()
    a = list(maps())
    b = a[:]
    a.sort()
    d = {}
    s = 0
    for i in range(n - 1):
        if a[i + 1] - a[i] > k:
            for j in range(s, i + 1):
                d[a[j]] = a[i]
            s = i + 1
    for i in range(s, n):
        d[a[i]] = a[n - 1]

    for i in range(p):
        u, v = map(lambda x: b[int(x) - 1], input().split())
        if (d[u] >= v and v >= u) or (d[v] >= u and u >= v):
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
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

    solve()
