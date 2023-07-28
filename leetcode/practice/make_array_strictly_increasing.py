class Solution:
    def makeArrayIncreasing(self, A: List[int], B: List[int]) -> int:
        n1, n2 = len(A), len(B)
        B.sort()

        def get_slightly_bigger(num):
            index = bisect.bisect_right(B, num)
            if index == n2:
                return None
            return B[index]

        @lru_cache(None)
        def recur(idx, atleast_bigger_than_this):
            """
            if A[idx] > A[idx-1]:
                1. then check if A[idx] can be made smaller or not
                2. do not do anything
            else:
                A[idx] <= A[idx-1]
                Check if A[idx] can be made slighty bigger than A[idx-1]
            """

            if idx == n1:
                return 0
            if A[idx] > atleast_bigger_than_this:
                res1 = recur(idx + 1, A[idx])
            else:
                res1 = float("inf")

            bigger = get_slightly_bigger(atleast_bigger_than_this)
            if bigger is None:
                res2 = float("inf")
            else:
                res2 = recur(idx + 1, bigger)
            return min(res1, res2 + 1)

        res = recur(0, float("-inf"))
        return res if res != float("inf") else -1
