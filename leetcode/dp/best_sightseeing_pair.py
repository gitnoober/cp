import collections

class Solution:
    def maxScoreSightseeingPair(self, values) -> int:
        n = len(values)
        sf, sfmx, res, mx = collections.deque(), -float('inf') , 0, values[0]

        for j in range(n-1, -1,-1):
            sfmax = max(sfmx, values[j] - j)
            sf.appendleft(sfmax)

        for i in range(1,n):
            res = max(res, mx + sf[i])
            mx = max(mx, values[i]+i)
        return res



values = [8,1,5,2,6]
# values = [1,2]
obj = Solution().maxScoreSightseeingPair(values)
print(obj)