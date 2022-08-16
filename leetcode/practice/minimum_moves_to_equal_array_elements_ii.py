class Solution:
    def minMoves2(self, nums) -> int:
        def findans(avg):
            res = 0
            for i in nums:
                res += abs(i - avg)
            return res

        n = len(nums)
        nums.sort()
        res = None
        if n % 2 == 0:
            res = findans((nums[n // 2 - 1] + nums[n // 2]) // 2)
        else:
            res = findans(nums[n // 2])
        return res


nums = [1, 0, 0, 8, 6]
obj = Solution().minMoves2(nums)
print(obj)
