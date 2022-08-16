class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0 for i in range(self.n + 1)]

    def get_sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def get_sum_segment(self, s, t):
        return self.get_sum(t) - self.get_sum(s - 1)

    def add(self, i, x):  # index , value
        while i <= self.n:
            # updating all the positions in the tree which are responsible for this index
            self.tree[i] += x
            i += i & -i


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        N = 1010
        tree = FenwickTree(N)
        for 


n = 3
k = 0
obj = Solution().kInversePairs(n, k)
print(obj)
