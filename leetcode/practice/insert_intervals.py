class Solution:
    def insert(self, intervals, newInterval):
        left, right, ans = [], [], []
        s, e = newInterval
        for i in intervals:
            if i[0] < s and i[1] < s:
                left += [i]
            elif i[0] > e and i[1] > e:
                right += [i]
            else:
                s, e = min(s, i[0]), max(e, i[1])
        [left] + [[s, e]] + [right]
        if left:
            ans = left
        ans += [[s, e]]
        if right:
            ans += right
        return ans


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
obj = Solution().insert(intervals, newInterval)
print(obj)
