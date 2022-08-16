class Solution:
    def generate(self, numRows: int):
        res = []
        numRows += 1

        def recur(i, arr):
            if i > numRows:
                return

            pes = [1] * i
            for j in range(1, i - 1):
                pes[j] = arr[j - 1] + arr[j]
            res.append(pes)
            recur(i + 1, pes)

        recur(1, [1])
        return res[-1]


numRows = 0
obj = Solution().generate(numRows)
print(obj)
