class Solution:
    def dsu(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1] * n
        self.numsets = n

    def find(self, x):
        xcopy = x
        while self.parents[x] != x:
            x = self.parents[x]

        while xcopy != x:
            xcopy, self.parents[xcopy] = self.parents[xcopy], x
        return x

    def union(self, u, v):
        a, b = self.find(u), self.find(v)
        if u != v:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.size[a] += self.size[b]  # sz.a > sz.b
            self.parents[b] = a

    def get_size(self, x):
        return self.size[self.find(x)]

    def longestConsecutive(self, nums) -> int:
        n = len(nums)
        self.dsu(n)
        d = {}
        vis = set()
        for i in range(n):
            if nums[i] in d:
                continue
            d[nums[i]] = [i]

        for idx, i in enumerate(nums):
            if i in vis:
                continue
            vis.add(i)
            if i - 1 in d:
                for j in d[i - 1]:
                    self.union(j, idx)
        ans = 0

        for i in range(n):
            ans = max(ans, self.get_size(i))
        return ans


nums = [1, 2, 0, 1]
obj = Solution().longestConsecutive(nums)
print(obj)
