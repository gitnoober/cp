class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        cnt = 0
        n = len(nums)
        for i in range(1, n - 1):
            if nums[i - 1] <= nums[i] <= nums[i + 1]:
                continue
            elif (
                nums[i - 1] > nums[i] <= nums[i + 1]
                and min(nums[i - 1], nums[i]) <= nums[i + 1]
            ):
                cnt += 1
                nums[i - 1] = nums[i] = min(nums[i - 1], nums[i])
            elif nums[i - 1] < nums[i] > nums[i + 1] and nums[i - 1] <= nums[i + 1]:
                nums[i] = nums[i + 1]
                cnt += 1
            elif nums[i - 1] <= nums[i] > nums[i + 1]:
                nums[i + 1] = nums[i]
                cnt += 1
            else:
                return False
        if cnt > 1:
            return False

        return True


nums = [5, 4, 3]
obj = Solution().checkPossibility(nums)
print(obj)

from itertools import permutations

ar = [3, 4, 5]
for i in permutations(ar, 3):
    print(i)
