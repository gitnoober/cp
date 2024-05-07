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


from collections import defaultdict


class Solution:
    def reversePairs(self, nums) -> int:
        N = len(nums)
        a = [(el, idx) for idx, el in enumerate(nums)]
        a.sort(key=lambda x: (x[0], -x[1]))
        arr = [0] * N
        cnt = 0
        defaultdict(int)
        i = 0
        # print(a)
        while i < N:
            x = a[i][0]
            j = i
            p = cnt
            while j < N and x == a[j][0]:
                j += 1
                p += 3
                cnt += 3

            f = j - 1
            while f >= i:
                arr[a[f][1]] = p
                p -= 3
                f -= 1
            # print(i, j, arr)
            i = j

        # cnt -= 1
        # print(arr)
        cnt = max(arr) + 1
        obj = FenwickTree(cnt)
        ans = 0
        for i in range(N - 1, -1, -1):
            j = arr[i] // 2
            print(j, i, arr, obj.get_sum(j - 1))
            s = obj.get_sum(j - 1)
            ans += s
            obj.add(arr[i], 1)
        # print(ans)
        return ans


# nums = [1, 3, 2, 3, 1]
# nums = [2, 4, 3, 5, 1]
nums = [2, -5, -5]
obj = Solution().reversePairs(nums)
print(obj)
