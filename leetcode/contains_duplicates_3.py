import heapq


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], k: int, t: int) -> bool:
        n = len(nums)

        def check(arr, min_val, max_val):
            l, r = 0, len(arr) - 1
            while l <= r:
                m = (l + r) >> 1
                if arr[m] < min_val:
                    l = m + 1
                elif arr[m] > max_val:
                    r = m - 1
                else:
                    return True

            return False

        for i in range(n):
            j = max(0, i - k)
            while j < n and j <= i + k:
                if j != i and abs(nums[i] - nums[j]) <= t:
                    return True
                j += 1
        return False


nums = [1, 2, 2, 3, 1]
k = 3
t = 0
obj = Solution().containsNearbyAlmostDuplicate(nums, k, t)
print(obj)
