
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
    # def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
    def friendRequests(self, n, restrictions, requests):
        dsu = DisjointSetUnion(n + 1)
        ans = []

        for x, y in requests:
            u, v = dsu.find(x), dsu.find(y)

            ok = True

            for a, b in restrictions:
                u1, v1 = dsu.find(a), dsu.find(b)

                if set([u1, v1]) == set([u, v]):
                    ok = False
                    break

            ans.append(ok)
            if ok:
                dsu.union(x, y)

        return ans


n = 7
restrictions = [[0, 6], [6, 2]]
requests = [[0, 2], [2, 3], [0, 2], [6, 4], [6, 4]]


ob = Solution()
x = ob.friendRequests(n, restrictions, requests)
print(x)
