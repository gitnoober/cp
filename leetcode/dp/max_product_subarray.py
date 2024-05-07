class Solution:
    def maxProduct(self, A) -> int:
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1

        return max(A + B)


nums = [-2, 0, -1]
obj = Solution().maxProduct(nums)
print(obj)
