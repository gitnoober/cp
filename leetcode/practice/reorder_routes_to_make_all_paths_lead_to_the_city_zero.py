from typing import List
from collections import defaultdict


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        gr = defaultdict(list)
        for u, v in connections:
            gr[u].append((v, 1))
            gr[v].append((u, 0))
        st = [0]
        vis = [False] * n
        vis[0] = True
        ans = 0
        for node in st:
            for child, d in gr[node]:
                if vis[child]:
                    continue
                ans += d
                vis[child] = True
                st.append(child)
        return ans


n = 5
connections = [[1, 0], [1, 2], [3, 2], [3, 4]]
# n = 6
# connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
obj = Solution().minReorder(n, connections)
