class Solution:
    def insert(self, intervals, newInterval):
        left, right = [], []
        s, e = newInterval
        for i in intervals:
            if i[0] < s and i[1] < s:
                left += [i]
                # print(i, "oioiujui")
            elif i[0] > e and i[1] > e:
                right += [i]
                # print(i, "ii")
            else:
                # print(i, "ii")
                s = min(s, i[0])
                e = max(e, i[1])
        x = [left] + [[s, e]] + [right]
        ans = []
        if left:
            ans = left
        ans += [[s, e]]
        if right:
            ans += right
        # print(ans, "ans")
        return ans


obj = Solution().insert(intervals, newInterval)
