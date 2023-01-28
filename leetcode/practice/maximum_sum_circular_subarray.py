class Solution:
    def maxSubarraySumCircular(self, nums) -> int:
        N = len(nums)
        max_suff_arr = [0] * N
        mx = nums[-1]
        summ = 0
        for i in range(N - 1, -1, -1):
            summ += nums[i]
            mx = max(mx, summ)
            max_suff_arr[i] = mx
        # print(max_suff_arr)
        summ = nums[0]
        curr_summ = 0
        ans = summ
        for i in range(N):
            curr_summ += nums[i]
            summ = max(summ, curr_summ)
            if curr_summ < 0:
                curr_summ = 0
            ans = max(ans, summ)

        summ = 0
        summx = 0
        for i in range(N - 1):
            summ += nums[i]
            summx = max(summ, summx)
            ans = max(ans, summx + max_suff_arr[i + 1])

        return ans


# 5 -3 5 5 -3 5


# nums = [1, -2, 3, -2]
# nums = [5, -3, 5]
# nums = [-3, -2, -3]
nums = [-2, 2, -2, 9]
obj = Solution().maxSubarraySumCircular(nums)
print(obj)
