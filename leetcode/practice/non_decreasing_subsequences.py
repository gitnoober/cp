class Solution:
    def findSubsequences(self, nums):
        ans = []
        st = []
        n = len(nums)
        vis = set()
        for i in range(n):
            st.append([[nums[i]], i])

        for arr, index in st:
            for j in range(index + 1, n):
                if nums[j] >= arr[-1]:
                    x = arr[:] + [nums[j]]
                    x_t = tuple(x)
                    if x_t in vis:
                        continue
                    ans.append(x)
                    st.append([x, j])
                    vis.add(x_t)
        return ans


nums = [4, 6, 7, 7]
obj = Solution().findSubsequences(nums)
print(obj)
