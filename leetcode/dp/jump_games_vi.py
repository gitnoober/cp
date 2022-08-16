from collections import deque


class Solution:
    def maxResult(self, nums, k: int):
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        d = deque()
        d.append([nums[0], 0])

        for i in range(1, n):
            dp[i] = d[0][0] + nums[i]

            while d and d[-1][0] < dp[i]:
                d.pop()

            d.append([dp[i], i])
            if d[0][1] < i - k:
                d.popleft(0)
        return dp[-1]
