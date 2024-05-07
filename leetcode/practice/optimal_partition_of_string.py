class Solution:
    def partitionString(self, s: str) -> int:
        d = set()
        n = len(s)
        j = 0
        ans = 1
        while j < n:
            if s[j] in d:
                d.clear()
                ans += 1
            d.add(s[j])
            j += 1

        return ans


s = "abacaba"
obj = Solution().partitionString(s)
print(obj)
