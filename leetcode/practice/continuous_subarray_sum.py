class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        s, d = 0, {}
        d[0] = 0
        for idx, i in enumerate(nums):
            s += i
            s %= k
            if s not in d:
                d[s] = idx + 1
            elif s in d and (idx + 1) - d[s] > 1:
                return True

        return False


nums = [23, 2, 4, 6, 6]
k = 7

obj = Solution().checkSubarraySum(nums, k)
print(obj)
