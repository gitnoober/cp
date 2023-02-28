class Solution:
    def firstMissingPositive(self, nums) -> int:
        n = len(nums)
        if n == 1:
            if nums[0] == 1:
                return 2
            return 1
        nums = [i if i > 0 and i < n else 0 for i in nums]
        st = []
        for i in range(n):
            if nums[i] <= 0:
                continue
            st.append(nums[nums[i]])
            nums[nums[i]] = -1
        for i in st:
            nums[i] = -1
        ans = n
        for i in range(1, n):
            if nums[i] == -1:
                continue
            ans = i
            break
        return ans


# nums = [1, 2, 0]
# nums = [3, 4, -1, 1]
nums = [1]
obj = Solution().firstMissingPositive(nums)
print(obj)
