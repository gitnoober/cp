class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        nums += [-1]
        cnt = 0
        ans = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                ans += cnt * (cnt+1)//2
                cnt = 0
                continue
            cnt += 1
        return ans
            
            
nums = [1,3,0,0,2,0,0,4]
obj = Solution().zeroFilledSubarray(nums)