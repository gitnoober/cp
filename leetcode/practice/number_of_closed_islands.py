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
    def closedIsland(self, grid: List[List[int]]) -> int:
        a = {}
        b = {}
        cnt = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                a[(i, j)] = cnt
                b[cnt] = (i, j)
                cnt += 1
        tree = DisjointSetUnion(cnt)
        dxdy = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        for i in range(n):
            for j in range(m):
                for dx, dy in dxdy:
                    X, Y = i + dx, j + dy
                    if (
                        X > -1
                        and X < n
                        and Y > -1
                        and Y < m
                        and grid[i][j] == grid[X][Y] == 0
                    ):
                        u, v = a[(i, j)], a[(X, Y)]
                        tree.union(u, v)
        dd = defaultdict(list)
        for i in range(cnt):
            y = b[i]
            if grid[y[0]][y[1]]:
                continue
            x = tree.find(i)
            dd[x].append(y)
        ans = 0
        for x in dd:
            ok = True
            for o, p in dd[x]:
                if o == 0 or p == 0 or o == n - 1 or p == m - 1:
                    ok = False
            if ok:
                ans += 1

        return ans


grid = [
    [
        1,
        1,
        1,
        0,
        0,
        0,
        1,
        0,
        1,
        1,
        1,
        1,
        1,
        0,
        0,
        0,
        1,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        1,
        1,
        0,
        1,
        1,
        0,
    ],
    [
        0,
        1,
        1,
        0,
        1,
        0,
        0,
        0,
        0,
        1,
        1,
        1,
        1,
        1,
        0,
        1,
        0,
        0,
        0,
        0,
        1,
        1,
        0,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
    ],
]
obj = Solution().closedIsland(grid)
print(obj)
