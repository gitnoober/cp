
import sys
import pprint
import logging
from logging import getLogger

def input(): return sys.stdin.readline().rstrip("\r\n")


logging.basicConfig(format="%(message)s", level=logging.WARNING,)
logger = getLogger(__name__)
logger.setLevel(logging.INFO)


def debug(msg, *args):
    logger.info(f'{msg}={pprint.pformat(args)}')

# 30 MINUTES ATLEAST !!!!


###################################################################################################################
from collections import defaultdict


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


n, m = map(int, input().split())
dsu = DisjointSetUnion(n + 1)
ok = True
inn = [0] * (n + 1)
for i in range(m):
    a, b = map(int, input().split())
    if dsu.find(a) == dsu.find(b):
        ok = False

    inn[a] += 1
    inn[b] += 1
    dsu.union(a, b)

cnt = 0
for i in range(1, n + 1):
    if inn[i] > 2:
        ok = False

print(['Yes', 'No'][ok ^ 1])
