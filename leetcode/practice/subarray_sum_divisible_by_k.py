from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums, k: int) -> int:
        prev, summ, ans = defaultdict(int), 0, 0
        for i in nums:
            summ += i
            summ %= k
            ans += prev[summ] + (summ == 0)
            prev[summ] += 1
        return ans


"""
Prev Solution:

if i == 0:
    if nums[i] % k == 0:
        ans += 1
else:
    ans += nums[i] % k == 0
    if summ == 0:
        # they are completed itseld, all those subarrays plus the including one
        ans += prev[summ] + 1
    elif summ != 0 and summ in prev:
        # they are missing, so inorder to have atleast prev[summ] sub-arrays
        ans += prev[summ]
    elif nums[i] % k == 0:
        ans += 1


[8], [8,9,7], [9,7], [9,7,8], [8], [8, 9, 7, 8], [7, 8, 9]
"""

nums = [8, 9, 7, 8, 9]
k = 8
obj = Solution().subarraysDivByK(nums, k)
print(obj)
