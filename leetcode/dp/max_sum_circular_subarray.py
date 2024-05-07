class Solution:
    def maxSubarraySumCircular(self, nums) -> int:
        max_sum, cur_max = nums[0], 0
        min_sum, cur_min = nums[0], 0
        tot = 0
        for i in nums:
            cur_max += i
            max_sum = max(max_sum, cur_max)
            if cur_max < 0:
                cur_max = 0

            cur_min += i
            min_sum = min(min_sum, cur_min)
            if cur_min > 0:
                cur_min = 0

            tot += i

        # print(max_sum, min_sum, tot)
        ans = max(tot - min_sum, max_sum) if max_sum > 0 else max_sum
        return ans


nums = [3, 1, 3, 2, 6]
obj = Solution().maxSubarraySumCircular(nums)
print(obj)
