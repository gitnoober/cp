class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zero_cnt, one_cnt, n, pre, summ, prev_ones = 0, 0, len(s), [], 0, 0
        for i in s:
            if i == "1":
                one_cnt += 1
            else:
                zero_cnt += 1
        ans = min(one_cnt, zero_cnt)
        for i in s:
            summ += int(i)
            pre.append(summ)
        if s[0] == "1":
            prev_ones += 1
        for i in range(1, n):
            rest_ones = pre[-1] - pre[i]
            rest_zeroes = (n - (i + 1)) - rest_ones  # convert them to ones
            ans = min(prev_ones + rest_zeroes, ans)
            prev_ones += int(s[i])
        return ans


s = "00110"
obj = Solution().minFlipsMonoIncr(s)
print(obj)
