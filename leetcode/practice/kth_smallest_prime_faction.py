from typing import List
from heapq import heappush, heappop


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        h = []
        for i in range(n):
            for j in range(i + 1, n):
                heappush(h, (arr[i] / arr[j], arr[i], arr[j]))

        while k > 1 and len(h) >= 2:
            k -= 1
            heappop(h)
        x = heappop(h)
        return [x[1], x[2]]
