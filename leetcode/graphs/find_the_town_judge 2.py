class Solution:
    def findJudge(self, n, trust):

        inn = [0] * n
        out = [0] * n
        for u, v in trust:
            inn[v - 1] += 1
            out[u - 1] += 1

        for i in range(n):
            if inn[i] == n - 1 and not out[i]:
                return i + 1
        return -1


n = 3
trust = [[1, 3], [2, 3], [3, 1]]
obj = Solution().findJudge(n, trust)
print(obj)
