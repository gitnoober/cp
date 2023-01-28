class Solution:
    def longestConsecutive(self, nums) -> int:
        d = {}
        op = {}
        for i in range(1, len(nums) + 1):
            d[nums[i - 1]] = i
            op[nums[i - 1]] = 1

        par = [i for i in range(10**5 + 10)]
        size = [1] * (10**5 + 10)

        def find(x):
            xcopy = x
            while x != par[x]:
                x = par[x]
            while xcopy != x:
                par[xcopy], xcopy = x, par[xcopy]
            return x

        def union(x, y):
            x, y = find(x), find(y)
            if x != y:
                if size[x] < size[y]:
                    size[y] += size[x]
                    par[x] = y
                else:
                    size[x] += size[y]
                    par[y] = x

        def get_size(x):
            return size[find(x)]

        for n in nums:
            if n - 1 in op:
                x = d[n]
                y = d[n - 1]
                union(x, y)
            if n + 1 in op:
                x = d[n]
                y = d[n + 1]
                union(x, y)

        ans = 0
        for i in nums:
            ans = max(ans, get_size(d[i]))
        return ans


nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
obj = Solution().longestConsecutive(nums)
print(obj)
