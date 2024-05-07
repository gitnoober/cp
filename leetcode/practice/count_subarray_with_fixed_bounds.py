from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        start = 0
        jmin = -1
        jmax = -1
        res = 0
        for i in range(n):
            if nums[i] > maxK or nums[i] < minK:
                start = i + 1
                jmin = -1
                jmax = -1

            if nums[i] == minK:
                jmin = i
            if nums[i] == maxK:
                jmax = i

            res += max(0, min(jmin, jmax) - start + 1)

        return res


nums = [1, 3, 5, 2, 7, 5]
minK = 1
maxK = 5
obj = Solution().countSubarrays(nums, minK, maxK)
print(obj)

# 3 - 5 + 1 = -1
# 3 - 4 = -1
