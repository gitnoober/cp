import sys


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


n = 100
dic = {}
cnt = 0
for i in range(n):
    for j in range(n):
        if (i, j) in dic:
            continue
        dic[(i, j)] = cnt
        cnt += 1


n = int(input())
arr = []
for _ in range(n):
    a = input()
    arr.append(a)

dsu = DisjointSetUnion(10010)
vis = [[False for _ in range(n)] for __ in range(n)]

d = [(0, -1), (0, 1), (-1, 0), (1, 0)]
q = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == "C":
            q.append((i, j))

for x, y in q:
    for dx, dy in d:
        X, Y = (x + dx), (y + dy)
        # print((x, y), (X, Y), dx, dy)
        if X > -1 and X < n and Y > -1 and Y < n and not vis[X][Y] and arr[X][Y] == "C":
            # vis[X][Y] = True
            q.append((X, Y))
            a = dic[(x, y)]
            b = dic[(X, Y)]
            # print((x, y), (X, Y))
            dsu.union(a, b)
    vis[x][y] = True
# print(dsu.parent)
ds = set()
ap = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == "C":
            f = dsu.find(dic[(i, j)])
            if f in ds:
                continue
            # print(f, i, j)
            ds.add(f)
            ap.append(dsu.set_size(f))

ap.sort(reverse=True)
ans = [0, 0]
for i in range(len(ap)):
    ans[i % 2] += ap[i]


sys.stdout.write(" ".join(map(str, ans)))
