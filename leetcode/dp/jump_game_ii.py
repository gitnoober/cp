class Solution:
    def jump(self, nums) -> int:
        steps = 0
        pos = len(nums) - 1

        while pos != 0:
            for i in range(pos):
                if nums[i] + i >= pos:
                    steps += 1
                    pos = i
                    break
        return steps


"""
Go from backward and find the farthest postion you could find from right so that a jump can
be possible to the current position.
"""


nums = [2, 3, 0, 1, 4]
obj = Solution().jump(nums)
print(obj)
