import heapq


class Solution:
    def halveArray(self, nums: list[int]) -> int:
        dec = sum(nums) / 2
        ans = 0
        h = []
        for i in nums:
            heapq.heappush(h, -i)
        while dec > 0:
            x = abs(heapq.heappop(h))
            dec -= x / 2
            heapq.heappush(h, -(x / 2))
            ans += 1
        return ans


nums = [5, 19, 8, 1]

obj = Solution().halveArray(nums)
print(obj)
