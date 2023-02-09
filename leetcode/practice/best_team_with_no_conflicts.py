class Solution:
    def bestTeamScore(self, scores, ages) -> int:
        n = len(scores)
        arr = [(i, j) for i, j in zip(ages, scores)]
        arr.sort(key=lambda x: (-x[0], -x[1]))
        dp = [0] * n
        # dp = [[0 for _ in range(MAXN)] for _ in range(n)]
        # dp[i][j] --- the maximum score till ith index
        for i in range(n):
            dp[i] = arr[i][1]
            for j in range(i):
                if arr[j][1] >= arr[i][1]:
                    dp[i] = max(dp[i], dp[j] + arr[i][1])
        return max(dp)


# scores = [1, 3, 5, 10, 15]
# ages = [1, 2, 3, 4, 5]

# scores = [4, 5, 6, 5]
# ages = [2, 1, 2, 1]

# scores = [1, 3, 7, 3, 2, 4, 10, 7, 5]
# ages = [4, 5, 2, 1, 1, 2, 4, 1, 4]

# scores = [6, 5, 1, 7, 6, 5, 5, 4, 10, 4]
# ages = [3, 2, 5, 3, 2, 1, 4, 4, 5, 1]

scores = [
    596,
    277,
    897,
    622,
    500,
    299,
    34,
    536,
    797,
    32,
    264,
    948,
    645,
    537,
    83,
    589,
    770,
]
ages = [18, 52, 60, 79, 72, 28, 81, 33, 96, 15, 18, 5, 17, 96, 57, 72, 72]
obj = Solution()
ans = obj.bestTeamScore(scores, ages)
print(ans)
