
class Solution:
    def minCostClimbingStairs(self, cost) -> int:

        n = len(cost)
        first, second = cost[0], cost[1]
        if n <= 2 :
            return min(first, second)

        for j in range(2,n):
            cur = cost[j] + min(first, second)
            first = second
            second = cur

        return min(first, second)






cost = [1,100,1,1,1,100,1,1,100,1]
obj = Solution().minCostClimbingStairs(cost)
print(obj)
