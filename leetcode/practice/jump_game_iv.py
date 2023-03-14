from typing import List
from collections import defaultdict


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        idx = defaultdict(list)
        for i in range(n):
            idx[arr[i]].append(i)
        q = [(0, 0)]
        step = float("inf")
        vis = [False] * n
        vis[0] = True
        for node, dis in q:
            if node == n - 1:
                step = min(step, dis)
                break
            nxt = idx[arr[node]]
            nxt.append(node + 1)
            nxt.append(node - 1)
            for adj in nxt:
                if adj > -1 and adj < n and not vis[adj]:
                    q.append((adj, dis + 1))
                    vis[adj] = True
            idx[arr[node]].clear()
        return step


arr = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]
# arr = [7]
# arr = [7, 6, 9, 6, 9, 6, 9, 7]
obj = Solution().minJumps(arr)

"""

dp[i] --- minimum steps needed to reach here


"""
