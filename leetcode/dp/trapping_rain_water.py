class Solution:
    def trap(self, height) -> int:
        n = len(height)
        max_left, max_right = [-float("inf") for _ in range(n)], [
            -float("inf") for _ in range(n)
        ]
        for i in range(n):
            if i == 0:
                max_left[i] = height[0]
            else:
                max_left[i] = max(height[i], max_left[i - 1])

        for i in range(n - 1, -1, -1):
            if i == n - 1:
                max_right[i] = height[i]
            else:
                max_right[i] = max(height[i], max_right[i + 1])

        ans = 0
        for i in range(1, n - 1):
            h = min(max_left[i - 1], max_right[i + 1])
            ans += max(0, h - height[i])
        return ans


height = [1]
obj = Solution().trap(height)
print(obj)

"""
Need zeroes in b/w to fill in water
        OR
if i < j and height[i] < height[j]


"""
