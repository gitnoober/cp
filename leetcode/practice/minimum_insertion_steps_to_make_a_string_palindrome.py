from functools import lru_cache


class Solution:
    def minInsertions(self, s: str) -> int:
        d =

        @lru_cache(None)
        def recur(s, cnt):
            i = 0
            j = len(s) - 1
            while i <= j and s[i] == s[j]:
                i += 1
                j -= 1
            s = s[i : j + 1]
            if len(s) == 0:
                return cnt
            # N = len()
            ans = min(recur(s[-1] + s, cnt + 1), recur(s + s[0], cnt + 1))
            return ans

        return recur(s, 0)


s = "mbadm"
# s = "zzazz"
s = "nezpxojlhylnnfliwgiuylsmkilzlssxgjodlqyjiwojqptlzuaizzoifkxrblxwmiwmcesqzymuafiqxsqduiuqedyftemktlgiznhajkoaqlwzukzzccjzzxvtplkjvutwrgbluejanbspdpgytfbscbizshxtshniwztxhljaisjxrrbkgxukgquqwegjbfjuldiydrucvsvhjgamadlurrwzpabrvlkhuznfiqoghfbx"
obj = Solution().minInsertions(s=s)
print(obj)
