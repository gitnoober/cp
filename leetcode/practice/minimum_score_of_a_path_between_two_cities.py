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

class Solution:
    def minScore(self, n: int, roads) -> int:
    	tree = DisjointSetUnion(n)
    	d = [float('inf')] * n
    	for u,v, di in roads:
    		u,v = u - 1, v - 1
    		tree.union(u,v)
    		x = min(d[v], d[u], di)
    		d[u] = x
    		d[v] = x
    	x = tree.find(0)
    	print(x)
    	ans = float('inf')
    	for i in range(n):
    		if tree.find(i) == x :
    			ans = min(ans, d[i])
    	return ans 


n = 4
roads = [[1,2,2],[1,3,4],[3,4,7]]
obj = Solution().minScore(n, roads
	)

print(obj)