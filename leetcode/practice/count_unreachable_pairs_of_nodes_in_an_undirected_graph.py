from typing import List
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

    def __len__(self):  # number of components
        return self.numsets


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        tree = DisjointSetUnion(n)
        for u, v in edges:
            tree.union(u, v)
        d = defaultdict(int)
        for i in range(n):
            d[tree.find(i)] += 1
        summ = 0
        for i in d:
            summ += d[i]
        # print(d)
        ans = 0
        for i in d:
            summ -= d[i]
            ans += tree.get_size(i) * summ
        return ans


n = 7
edges = [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]
obj = Solution().countPairs(n, edges)
print(obj)
