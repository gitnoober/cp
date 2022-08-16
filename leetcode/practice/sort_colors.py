class Solution:
    def sortColors(self, a) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(a)
        i = 0
        for j in range(n):
            if a[j] == 0:
                a[j], a[i] = a[i], a[j]
                i += 1
        for j in range(n):
            if a[j] == 1:
                a[j], a[i] = a[i], a[j]
                i += 1
        return a


a = [2, 0, 2, 1, 1, 0]
obj = Solution().sortColors(a)
print(obj)
