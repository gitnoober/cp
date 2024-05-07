class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        """
        Dp solution
        dp[i][j] - true if from idx i to idx j the string is palindromic
        dp = [[0 for _ in range(n+1)] for __ in range(n+1)]
        mx, st,end = 0, 0,0
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i] == s[j]:
                    dp[i][j] = j - i < 3 or dp[i+1][j-1]
                    if dp[i][j]:
                        st = i
                        end = j + 1
                        mx = j - i + 1
        return s[st:end]
        """

        mx = 0
        i1, i2 = 0, 1
        for i in range(n):

            end = i
            while end < n and s[end] == s[i]:
                end += 1
            start = i - 1
            while start >= 0 and end < n and s[start] == s[end]:
                start -= 1
                end += 1

            if end - start - 1 > mx:
                mx = end - start - 1
                i1, i2 = start + 1, end
        return s[i1:i2]


s = "aba"
obj = Solution().longestPalindrome(s)
print(obj)
