class Solution:
    def candy(self, ratings) -> int:
        n = len(ratings)
        L, R = [1] * n, [1] * n
        ans = 0

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                L[i] = L[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                R[i] = R[i + 1] + 1

        for i in range(n):
            ans += max(L[i], R[i])
        return ans


# ratings = [1, 2, 87, 87, 87, 2, 1]
ratings = [1, 0, 2]
obj = Solution().candy(ratings)
print(obj)

# 1 2 3 4 1
