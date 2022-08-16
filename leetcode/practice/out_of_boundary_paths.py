from functools import lru_cache


class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        DIR = [0, 1, 0, -1, 0]

        @lru_cache(None)
        def dp(r, c, maxMove):
            if r < 0 or r == m or c < 0 or c == n:
                return 1  # Out of bound -> Count 1 way
            if maxMove == 0:
                return 0
            ans = 0
            for i in range(4):
                ans = (
                    ans + dp(r + DIR[i], c + DIR[i + 1], maxMove - 1)
                ) % 1_000_000_007
            return ans

        return dp(startRow, startColumn, maxMove)


m = 2
n = 2
maxMove = 2
startRow = 0
startColumn = 0
obj = Solution().findPaths(m, n, maxMove, startRow, startColumn)
print(obj)
