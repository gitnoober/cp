# DON'T SUBMIT UNLESS YOU'RE ABSOLUTELY SURE OR ATLEAST 70 % SURE !!!

import sys
import pprint
import logging
from logging import getLogger
import array
import collections
import io
import os
import heapq
import bisect

# sys.setrecursionlimit(10 ** 9)

inf = float("inf")
# mod = int(1e9) + 7
# mod = 998244353


def check(dic, length):
    ct = 0
    for i in dic:
        if dic[i] % 2:
            ct += 1

    if (length % 2 and ct == 1) or ():
        return True


class Solution:
    def kConcatenationMaxSum(self, arr: list[int], k: int) -> int:
        sm = sum(arr)

        def kadane(arr):
            curmx = mx = 0
            for i in arr:
                curmx += i
                if curmx < 0:
                    curmx = 0
                mx = max(mx, curmx)
            return mx

        ans = max(
            0,
            kadane(arr),
            kadane(min(k, 2) * arr),
            sm * k,
            kadane(arr) + sm * (k - 1),
        )

        ans %= int(1e9 + 7)
        return ans


arr = [-5, -2, 0, 0, 3, 9, -2, -5, 4]
k = 5

obj = Solution().kConcatenationMaxSum(arr, k)
print(obj)


# if __name__ == "__main__":
#     # input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

#     def linp():
#         return [int(i) for i in input().split()]

#     logging.basicConfig(
#         format="%(message)s",
#         level=logging.WARNING,
#     )
#     logger = getLogger(__name__)
#     logger.setLevel(logging.INFO)

#     def debug(msg, *args):
#         logger.info(f"{msg}={pprint.pformat(args)}")

#     print(solve())
