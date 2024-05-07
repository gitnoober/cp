# DON'T SUBMIT UNLESS YOU'RE ABSOLUTELY SURE OR ATLEAST 70 % SURE !!!

import pprint
import logging
from logging import getLogger
import io
import os

# sys.setrecursionlimit(10 ** 9)

inf = float("inf")
# mod = int(1e9) + 7
# mod = 998244353


class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)


def solve():

    n, d = linp()
    dsu = DisjointSetUnion(n)
    A = [linp() for _ in range(d)]
    res = []
    cnt = 1

    for u, v in A:
        u -= 1
        v -= 1

        if dsu.find(u) == dsu.find(v):
            cnt += 1  # number of instructions you can save
        dsu.union(u, v)

        ans = []
        for i in range(n):
            if dsu.find(i) == i:
                ans.append(dsu.set_size(i))

        ans.sort(reverse=True)

        tmp = 0
        # utilize the saved instructions by joining the biggest components
        for k in range(min(len(ans), cnt)):
            tmp += ans[k]

        res.append(tmp)

        # debug("ans", ans) #you need to perform exactly i introductions , provided all the previous people are already connected!

    """
    so all the people till i need to be connected and if you have any saved introductions you can use them to connect to the
    largest components you know
    """

    print(*[i - 1 for i in res], sep="\n")


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
