class Solution:
    def rob(self, nums) -> int:
        
        n = len(nums)
        def dp(l,r):
            pre = cur = 0
            for i in range(l,r+1):
                temp = max(nums[i]+ pre, cur)
                pre = cur
                cur = temp
            return cur


        if n < 2 :
            return nums[0]

        return max(dp(0,n-2), dp(1, n-1))








nums = [1 ,2 ,3]
obj = Solution().rob(nums)
print(obj)