from functools import lru_cache


class Solution:
    def minCost(self, houses, cost, m: int, n: int, target: int) -> int:
        @lru_cache
        def check(a, c):
            i = 0
            cnt = 0
            n = len(a)
            while i < n:
                j = i + 1
                while j < n and a[j] == a[i]:
                    j += 1
                i = j
                cnt += 1
            return cnt == c

        @lru_cache
        def recur(idx, cst, arr):
            if idx == m:
                if check(arr, target):
                    return cst
                return float("inf")

            ans = float("inf")

            if houses[idx] == 0:
                for j in range(n):
                    res = recur(idx + 1, cst + cost[idx][j], arr + (j + 1,))
                    ans = min(ans, res)
            else:
                res = recur(idx + 1, cst, arr + (houses[idx],))
                ans = min(ans, res)
            return ans

        ans = recur(0, 0, ())

        return -1 if ans == float("inf") else ans


houses = [0, 2, 1, 2, 0]
cost = [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]]
m = 5
n = 2
target = 3
obj = Solution().minCost(houses, cost, m, n, target)
print(obj)
