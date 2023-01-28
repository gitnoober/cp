class Solution:
    def wiggleMaxLength(self, nums):
        n = len(nums)
        dp = [[1 for _ in range(n)] for __ in range(2)]
        """
        extending previous subsequence
        starting new one
        or just ignoring this
        """
        for i in range(1, n):
            x = nums[i] - nums[i - 1]
            if x > 0:
                dp[0][i] = max(dp[1][i - 1] + 1, dp[0][i], dp[0][i - 1])
            elif x < 0:
                dp[1][i] = max(dp[0][i - 1] + 1, dp[1][i], dp[1][i - 1])
            else:
                dp[0][i] = dp[0][i - 1]
                dp[1][i] = dp[1][i - 1]
        return max(dp[0][-1], dp[1][-1])


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
obj = Solution().wiggleMaxLength(nums)
print(obj)
