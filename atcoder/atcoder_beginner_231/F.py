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
from collections import defaultdict, deque
from copy import deepcopy


def naive(a, b):
    ans = set()
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] >= a[j] and b[i] <= b[j]:
                ans.add((i, j))
    return len(ans)


class FenwickTree:
    def __init__(self, x):
        """transform list into BIT"""
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] += x[i]

    def add(self, idx, x):
        """updates bit[idx] += x"""
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1

    def query(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def findkth(self, k):
        """Find largest idx such that sum(bit[:idx]) <= k"""
        idx = -1
        for d in reversed(range(len(self.bit).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(self.bit) and k >= self.bit[right_idx]:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
A = list(zip(a, b))
A.sort(key=lambda x: x[0], reverse=True)
tree1 = FenwickTree([0 for i in range(n + 1)])
tree2 = FenwickTree([0 for i in range(n + 1)])
a1 = sorted([i, idx] for idx, i in enumerate(a))
b1 = sorted([i, idx] for idx, i in enumerate(b))
d1, d2 = defaultdict(deque), defaultdict(deque)

for i, j in a1:
    d1[i].append(j)

for i, j in b1:
    d2[i].append(j)

dd1, dd2 = deepcopy(d1), deepcopy(d2)

a.sort()
b.sort()
for i in range(n):
    idx = d1[a[i]].popleft()
    tree1.add(idx, 1)
    idx = d2[b[i]].popleft()
    tree2.add(idx, 1)

ans = 0
for i in range(n - 1, -1, -1):
    ai, bi = A[i]
    i1, i2 = dd1[ai].pop(), dd2[bi].pop()
    # now check all those aj's which are less
    x1 = tree1.query(i1)
    x2 = tree2.query(n + 1) - tree2.query(i2)
    tree1.add(i1, -1)
    tree2.add(i2, -1)
    ans += x1 + x2

print(ans)


ans = naive(a, b)
