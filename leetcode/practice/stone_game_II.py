from typing import List
from functools import lru_cache


class Solution:
    def stoneGameII(self, A: List[int]) -> int:
        n = len(A)
        for i in range(n - 2, -1, -1):
            A[i] += A[i + 1]

        @lru_cache(None)
        def dp(i, m):
            if i + 2 * m >= n:
                return A[i]

            return A[i] - min(dp(i + x, max(m, x)) for x in range(1, 2 * m + 1))

        return dp(0, 1)


piles = [2, 7, 9, 4, 4]
obj = Solution().stoneGameII(piles)
print(obj)
