import math


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def check(mid, need):
            x = (
                mid // a
                + mid // b
                + mid // c
                - mid // ab
                - mid // bc
                - mid // ac
                + mid // abc
            )
            return x >= need

        ab = (a * b) // math.gcd(a, b)
        bc = (b * c) // math.gcd(b, c)
        ac = (a * c) // math.gcd(a, c)
        abc = (ab * c) // math.gcd(ab, c)
        l, h = 0, 10**10
        ans = 0
        while l <= h:
            m = (l + h) >> 1
            if check(m, n):
                ans = m
                h = m - 1
            else:
                l = m + 1
        return ans


n, a, b, c = 5, 2, 3, 3
obj = Solution().nthUglyNumber(n, a, b, c)
print(obj)
