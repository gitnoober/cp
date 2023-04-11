from functools import lru_cache


class Solution:
    def maxSatisfaction(self, a) -> int:
        a.sort()
        res = total = 0
        while a and a[-1] + res > 0:
            res += a.pop()
            total += res
        return total


satisfaction = []

obj = Solution().maxSatisfaction(satisfaction)
print(obj)
