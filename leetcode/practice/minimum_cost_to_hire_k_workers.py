from typing import List
from heapq import heappush, heappop


class Solution:
    def mincostToHireWorkers(self, q: List[int], w: List[int], k: int) -> float:
        ans = float("inf")
        a = [(j / i, i) for i, j in zip(q, w)]
        a.sort()
        h = []
        qsum = 0
        ans = float("inf")
        for i in a:
            qsum += i[1]
            heappush(h, -i[1])  # push quality into heap
            if (
                len(h) > k
            ):  # if length of h > k, then pop out the biqqest quality from pool
                qsum += heappop(h)
            if len(h) == k:
                ans = min(ans, qsum * i[0])
        return ans
