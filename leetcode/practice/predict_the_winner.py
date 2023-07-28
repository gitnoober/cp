from typing import List


class Solution:
    def __init__(self):
        self.nums = None
        self.dp = {}

    def recur(self, i, j):
        if (i, j) not in self.dp:
            if i == j:
                return self.nums[i]
            self.dp[(i, j)] = max(
                self.nums[i] - self.recur(i + 1, j), self.nums[j] - self.recur(i, j - 1)
            )
        return self.dp[(i, j)]

    def PredictTheWinner(self, nums: List[int]) -> bool:
        self.nums = nums
        n = len(self.nums)
        return self.recur(0, n - 1) >= 0


num_arr = [1, 5, 2]
num_arr = [1, 5, 233, 7]
obj = Solution().PredictTheWinner(nums=num_arr)
print(obj)
