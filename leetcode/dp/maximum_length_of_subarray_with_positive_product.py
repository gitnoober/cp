
class Solution:
    def getMaxLen(self, nums) -> int:
        n = len(nums)
        pos, neg, ans = 0 , 0 , 0
        for i in range(n):
            if nums[i] > 0 :
                pos, neg = pos + 1 , neg + 1 if neg else 0
            elif nums[i] < 0 :
                pos, neg = 1 + neg if neg else 0, 1 + pos
            else:
                pos, neg = 0, 0
            ans = max(ans, pos)

        return ans

nums = [1,-2,-3,4]
obj = Solution().getMaxLen(nums)
print(obj)