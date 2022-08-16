from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        # @lru_cache
        # def recur(i):
        #     res = 0
        #     if i == len(s):
        #         return 1

        #     if i < n and s[i] != "0":
        #         res += recur(i + 1)

        #     if i + 1 < n and s[i] != "0" and int(s[i] + s[i + 1]) <= 26:
        #         res += recur(i + 2)

        #     return res

        # return recur(0)
        dp = [0] * (n + 1)
        dp[-1] = 1
        for i in range(n - 1, -1, -1):
            if s[i] != "0":
                dp[i] = dp[i + 1]

            if i + 1 < n and s[i] != "0" and int(s[i] + s[i + 1]) <= 26:
                dp[i] += dp[i + 2]

        # print(dp)

        return dp[0]


s = "12"
obj = Solution().numDecodings(s)
print(obj)
