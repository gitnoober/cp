
class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        n = len(cost)
        dp = [0 for i in range(n)]
        
        def recur(i):
            if i < 0 :
                return 0
            if i <= 1 :
                return cost[i]
            return cost[i] + min(recur(i-1), recur(i-2))

        # x = min(recur(n-1), recur(n-2))
        # print(x)
        for i in range(n):
            if i < 2 :
                dp[i] = cost[i]
            else:
                dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        return min(dp[-1], dp[-2])






cost = [10,15,20]
obj = Solution().minCostClimbingStairs(cost)
print(obj)
