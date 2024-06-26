class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0 for _ in range(n2 + 1)] for __ in range(n1 + 1)]
        self.ans = float("inf")
        for i in range(n1 + 1):
            dp[0][i] = i
        for i in range(n2 + 1):
            dp[i][0] = i

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[n1][n2]


word1 = "intention"
word2 = "execution"
obj = Solution().minDistance(word1, word2)
print(obj)
