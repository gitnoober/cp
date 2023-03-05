from typing import List
from collections import defaultdict


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [float("inf")] * n
        dp[-1] = 0
        # dp[1] = 1
        # tree = defaultdict(list)
        idx = defaultdict(list)
        for i in range(n):
            idx[arr[i]].append(i)
        print(idx)
        for i in range(n - 1, -1, -1):
            for j in idx[arr[i]]:
                dp[j] = min(dp[j], dp[i] + 1)

            if i + 1 < n:
                dp[i] = min(dp[i], dp[i + 1] + 1)
            if i - 1 > -1:
                dp[i] = min(dp[i], dp[i - 1] + 1)
                for j in idx[arr[i - 1]]:
                    if j > i:
                        break
                    dp[j] = min(dp[j], dp[i] + 1)

        # print(dp)
        return dp[0]


# arr = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]
arr = [7]
arr = [7, 6, 9, 6, 9, 6, 9, 7]
obj = Solution().minJumps(arr)

"""

dp[i] --- minimum steps needed to reach here


"""
