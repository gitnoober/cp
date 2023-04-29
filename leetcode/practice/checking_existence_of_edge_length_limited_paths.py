from typing import List


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
    def distanceLimitedPathsExist(
        self, n: int, edgeList: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        queries = sorted([(w, u, v, i) for i, (u, v, w) in enumerate(queries)])
        edges = sorted([(w, u, v) for u, v, w in edgeList])
        ans = [0] * len(queries)
        ii = 0
        tree = DisjointSetUnion(100005)
        # print(queries)
        # print(edges)
        for w, u, v, i in queries:
            while ii < len(edges) and edges[ii][0] < w:
                a, b, c = edges[ii]
                tree.union(b, c)
                ii += 1
            ans[i] = tree.find(u) == tree.find(v)
        return ans
