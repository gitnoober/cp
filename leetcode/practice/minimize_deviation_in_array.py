from heapq import heappush, heappop


class Solution:
    def minimumDeviation(self, nums) -> int:
        h = []
        mi = float("inf")
        ans = float("inf")
        for i in nums:
            x = 2 * i if i % 2 else i
            mi = min(mi, x)
            heappush(h, -x)

        while h:
            x = -heappop(h)
            ans = min(ans, x - mi)
            if x % 2:
                break
            mi = min(mi, x // 2)
            heappush(h, -(x // 2))
        return ans


nums = [1, 2, 3, 4]
# nums = [3, 5]
obj = Solution().minimumDeviation(nums)
print(obj)
"""

100,2, 4, 4, 4, 4

ans = 98
50, 2, 4
ans = 48
25, 2, 4


6, 10
ans = 4
5, 6
ans = 0
5, 3



"""
