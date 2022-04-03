class Solution:
    def maximumTop(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return -1 if k % 2 else nums[0]

        if k <= n:
            mx = nums[0] if k - 1 > 0 else 0
            for i in range(k - 1):
                mx = max(mx, nums[i])
            if k < n:
                mx = max(mx, nums[k])
            return mx

        return max(nums)


nums = list(map(int, input().split(",")))
k = 1000000000
obj = Solution().maximumTop(nums, k)
print(obj)
