class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        # print(dp)
        return min(dp[-1], dp[-2])


cost = [0, 0, 0, 1]
# cost = [10, 15, 20]
# cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
obj = Solution().minCostClimbingStairs(cost)
print(obj)
