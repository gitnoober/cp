class MakeAllOne:
    # DO NOT read from stdin or write to stdout
    # Input is given as function argument
    # Output is taken as the function return value
    def getMinimumMoves(self, nums, K):
        # pass # Code here
        n = len(nums)
        d = {0: []}
        ans = 0
        for i in range(n):
            if nums[i] == 0:
                d[nums[i]].append(i)

        if len(d[0]) == 0:
            return 0

        i = 0
        while i < len(d[0]):
            j = i + 1
            while j < len(d[0]) and d[0][j] - d[0][i] + 1 <= K:
                j += 1
            i = j
            ans += 1
        return ans


nums = [0, 0, 1, 0, 0]
K = 2
ob = MakeAllOne()
x = ob.getMinimumMoves(nums, 5)
print(x)
