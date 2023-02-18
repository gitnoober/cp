from collections import defaultdict, deque
from math import ceil


class Solution:
    def minimumFuelCost(self, roads, seats: int) -> int:
        tree = defaultdict(set)
        self.ans = 0
        for u, v in roads:
            tree[u].add(v)
            tree[v].add(u)

        def dfs(node, prev, people=1):
            for nei in tree[node]:
                if nei == prev:
                    continue
                people += dfs(nei, node)

            self.ans += ceil(people / seats) if node else 0
            return people

        dfs(0, -1)

        # print(self.ans, "pp")

        return self.ans


roads = [[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]]
seats = 2
obj = Solution().minimumFuelCost(roads, seats)
