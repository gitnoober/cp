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
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # N = 10**5 + 5

        tree_a = DisjointSetUnion(n)
        tree_b = DisjointSetUnion(n)
        ans = 0
        for type_, u, v in edges:
            u, v = u - 1, v - 1
            if type_ == 1:
                x, y = tree_a.find(u), tree_a.find(v)
                if x != y:
                    tree_a.union(u, v)
                else:
                    ans += 1
            elif type_ == 2:
                x, y = tree_b.find(u), tree_b.find(v)
                if x != y:
                    tree_b.union(u, v)
                else:
                    ans += 1
            else:
                x1, y1 = tree_a.find(u), tree_a.find(v)
                x2, y2 = tree_b.find(u), tree_b.find(v)
                if x1 != y1 or x2 != y2:
                    tree_a.union(u, v)
                    tree_b.union(u, v)
                else:
                    ans += 1
        # print(tree_a.__len__(), tree_b.__len__())
        res = ans if tree_a.__len__() == tree_b.__len__() == 1 else -1
        return res


n = 4
# edges = [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]
edges = [[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]]
obj = Solution().maxNumEdgesToRemove(n, edges)
print(obj)
