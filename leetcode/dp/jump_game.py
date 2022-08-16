

class Solution:
    def canJump(self, nums) -> bool:
        n = len(nums)
        # dp = [False]*n
        # dp[-1] = True
        # for j in range(n-2,-1,-1):
        #     for i in range(j, min(j+nums[j] , n - 1)+1):
        #         if dp[i]:
        #             dp[j] = True
        # return dp[0]
        target = n - 1
        for i in range(n-2,-1,-1):
            if i + nums[i] >= target:
                target = i
        return target == 0








nums = [2,3,1,1,4]
obj = Solution().canJump(nums)
print(obj)




"""

can jump <= nums]idx]


"""