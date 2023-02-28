class Solution:
    def searchInsert(self, nums, target) -> int:
        n = len(nums)
        self.index = -1
        l = 0
        h = n - 1
        while l <= h:
            m = (l + h) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                self.index = m
                l = m + 1
            else:
                h = m - 1
        return self.index + 1


nums = [1, 3, 5, 6]
target = 5


obj = Solution().searchInsert(nums, target)
print(obj)
