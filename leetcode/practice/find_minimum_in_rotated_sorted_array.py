class Solution:
    def findMin(self, nums: list[int]) -> int:
        def binary(arr, l, h):
            len(arr)
            mx = float("inf")
            while l <= h:
                m = (l + h) >> 1
                if arr[m] > arr[m + 1]:
                    mx = min(mx, arr[m + 1])
                    l = m + 1
                else:
                    mx = min(mx, binary(arr, l, m - 1), binary(arr, m + 1, h))
                    h = m - 1
            return mx

        mx = binary(nums, 0, len(nums) - 2)
        return min(mx, nums[0])


nums = [11, 13, 15, 17]
obj = Solution().findMin(nums)
