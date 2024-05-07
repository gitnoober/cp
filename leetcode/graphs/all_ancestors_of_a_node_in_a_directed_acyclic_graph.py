import collections


class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        gr = collections.defaultdict(list)
        levels = collections.defaultdict(set)
        for u, v in edges:
            gr[u].append(v)

        def dfs(u, p, vis):
            vis.add(u)
            if p != -1:
                levels[u].add(p)
                levels[u] |= levels[p]

            for v in gr[u]:
                if v not in vis:
                    dfs(v, u, vis)

        for i in range(n):
            vis = set()
            dfs(i, -1, vis)

        ans = []
        for i in range(n):
            ans.append(sorted(levels[i]))
        return ans


n = 8
edgeList = [
    [0, 7],
    [7, 6],
    [0, 3],
    [6, 3],
    [5, 4],
    [1, 5],
    [2, 7],
    [3, 5],
    [3, 1],
    [0, 5],
    [7, 5],
    [2, 1],
    [1, 4],
    [6, 1],
]
# n = 8
# edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
obj = Solution().getAncestors(n, edgeList)
print(obj)
