from typing import List
from math import ceil


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = 0
        summ = 0
        for idx, num in enumerate(nums):
            summ += num
            res = max(res, ceil(summ / (idx + 1)))
        return res


nums = [13, 13, 20, 0, 8, 9, 9]
# nums = [6, 9, 3, 8, 14]
obj = Solution().minimizeArrayValue(nums)
print(obj)
