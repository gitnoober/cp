from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        miss = [0] * 10000
        for i in arr:
            miss[i] = True
        i = 1
        while i < 10000 and k > 0:
            if not miss[i]:
                k -= 1
            i += 1

        return i - 1


arr = [2, 3, 4, 7, 11]
k = 5
obj = Solution().findKthPositive(arr, k)
print(obj)
