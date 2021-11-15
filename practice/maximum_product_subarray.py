class MaximumProductSubarray:
    # DO NOT read from stdin or write to stdout
    # Input is given as function argument
    # Output is taken as the function return value
    def getMaximumProduct(self, nums):
        ans = -99999999999999999999999999999999999999999
        left_pr, right_pr = 1, 1
        for i in range(len(nums)):
            left_pr *= nums[i]
            if left_pr > ans:
                ans = left_pr

            if left_pr == 0:
                left_pr = 1

        for i in range(len(nums) - 1, -1, -1):
            right_pr *= nums[i]
            if right_pr > ans:
                ans = right_pr

            if right_pr == 0:
                right_pr = 1
        return ans


ob = MaximumProductSubarray()
nums = [4, 2, -2, 100, 10]
x = ob.getMaximumProduct(nums)
print(x)
