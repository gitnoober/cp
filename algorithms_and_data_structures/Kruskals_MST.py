"""
    Algorithm for finding a MST

    1) Sort all the edges with respect to their weights and pick the minimum one
    2) Check if it forms a cycle with the mstset(set of vertices picked for MST)
    3) If it doesn't add it to the mstset
"""


class Kruskal:

    def __init__(self, graph, n):
        self.n = n
        self.gr = graph
        self.par = [i for i in range(self.n)]
        self.sz = [1 for i in range(self.n)]

    def find(self, x):
        xcopy = x

        while x != self.par[x]:
            x = self.par[x]

        while xcopy != x:
            xcopy, self.par[xcopy] = self.par[xcopy], x

        return xcopy

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            if self.sz[x] < self.sz[y]:
                x, y = y, x

            self.par[y] = x
            self.sz[x] += self.sz[y]

    def findmst(self):
        self.gr.sort(
            key=lambda x: x[2]
        )  # assuming weights is the third element in the tuple
        res = []
        i = e = 0
        summ = 0
        while e < self.n - 1:
            u, v, w = self.gr[i]
            i += 1

            if self.find(u) == self.find(v):
                continue

            e += 1
            res.append([u, v, w])
            self.union(u, v)
            summ += w

        return res, summ


# edges = []
# for i in range(5):
#     u, v, wt = map(int, input().split())
#     edges.append((u, v, wt))

# obj = Kruskal(edges, 4)

# print(obj.findmst())

# number of vertices remain the same,just the edges you have to pick v - 1  of them
