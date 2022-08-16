
class Solution:
    def numberOfArithmeticSlices(self, nums) -> int:
        n = len(nums)
        cnt = 1
        prev = None
        res = 0
        for i in range(n-1):
            if prev is None or prev == nums[i] - nums[i+1]:
                cnt+=1
            else:
                all_ = max(0, (cnt*(cnt+1)//2) - (cnt - 1 + 1) - (cnt - 2 + 1))
                res+=all_
                cnt=2
            prev = nums[i] - nums[i+1]
        all_ = max(0, (cnt*(cnt+1)//2) - (cnt - 1 + 1) - (cnt - 2 + 1))
        res+=all_

        return res










nums = [1,2,3,4]
obj = Solution().numberOfArithmeticSlices(nums)
print(obj)
        