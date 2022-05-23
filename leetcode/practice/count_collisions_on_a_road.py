import collections


class Solution:
    def countCollisions(self, directions: str) -> int:

        n = len(directions)
        ans = 0
        i, j = 0, n - 1
        while i < j and directions[i] == "L":
            i += 1
        while i < j and directions[j] == "R":
            j -= 1
        ans = 0
        for k in range(i, j + 1):
            if directions[k] != "S" and i != j:
                ans += 1
        return ans


directions = "LLRR"
obj = Solution().countCollisions(directions)
print(obj)

# R - L -- 2
# R - S -- 1
# 2 - 4
