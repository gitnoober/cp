class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        dp = [-1] * n

        def recur(i):
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]

            dp[i] = max(nums[i] + recur(i + 2), recur(i + 1))
            return dp[i]

        # return recur(0)
        for i in range(n):
            for j in range(i + 1, n):
                dp[i] = max(nums[i])


nums = [2, 7, 9, 3, 1]
obj = Solution().rob(nums)
print(obj)
