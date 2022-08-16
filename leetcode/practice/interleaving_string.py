from functools import lru_cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 + n2 != len(s3):
            return False
        ok = False

        @lru_cache
        def recur(i, j, k, st):
            nonlocal ok
            if k == n1 + n2 and i == n1 and j == n2:
                return st == s3

            x = False
            if i < n1 and s1[i] == s3[k]:
                x = recur(i + 1, j, k + 1, st + s3[k])

            if j < n2 and s2[j] == s3[k]:
                x = recur(i, j + 1, k + 1, st + s3[k])

            ok |= x
            return ok

        x = recur(0, 0, 0, "")
        return x


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
# s1, s2, s3 = "", "", ""
# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbbaccc"
# s1 = "a"
# s2 = ""
# s3 = "a"
# s1 = "abababababababababababababababababababababababababababababababababababababababababababababababababbb"
# s2 = "babababababababababababababababababababababababababababababababababababababababababababababababaaaba"
# s3 = "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababbb"
obj = Solution().isInterleave(s1, s2, s3)
print(obj)
