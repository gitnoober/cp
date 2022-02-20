class Solution:
    def maximumEvenSplit(self, finalSum: int) -> list[int]:
        s = 0
        arr = []
        n = 2
        while s < finalSum:
            s += n
            arr.append(n)
            n += 2
        diff = s - finalSum
        # print(arr)
        if diff in arr or diff == 0:
            if diff:
                arr.remove(diff)
            return arr
        return []

finalSum = 12
obj = Solution().maximumEvenSplit(finalSum)
print(obj)
