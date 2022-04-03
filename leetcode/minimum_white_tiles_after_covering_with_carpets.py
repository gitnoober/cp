import sys
from functools import lru_cache

sys.setrecursionlimit(2200)


class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        @lru_cache(None)
        def recur(pos, used):
            if used < 0:
                return float("inf")
            if pos < 0:
                return 0

            return min(
                int(floor[pos]) + recur(pos - 1, used),
                recur(pos - carpetLen, used - 1),
            )

        n = len(floor)
        return recur(n - 1, numCarpets)


floor = "10110101"
numCarpets = 2
carpetLen = 2
obj = Solution().minimumWhiteTiles(floor, numCarpets, carpetLen)
print(obj)
