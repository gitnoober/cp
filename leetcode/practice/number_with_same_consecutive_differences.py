class Solution:
    def numsSameConsecDiff(self, n: int, k: int):
        ans = set()

        def recur(num, l):
            if l == n:
                ans.add(num)
                return
            if num == 0:
                for i in range(1, 10):
                    recur(i, 1)
            else:
                last_num = num % 10
                common = num * 10
                if last_num - k > -1:
                    recur(common + (last_num - k), l + 1)
                if last_num + k < 10:
                    recur(common + (last_num + k), l + 1)

        recur(0, 0)

        return list(ans)


n = 2
k = 0
ans = Solution().numsSameConsecDiff(n, k)
print(ans)
